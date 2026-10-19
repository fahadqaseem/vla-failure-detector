"""PNR scan over failed episodes (definition in CLAUDE.md).

Default is a fast backward scan: start at the last checkpoint and walk earlier until a checkpoint is no
longer "bad" (fewer than min_fail of K replays fail). That finds the same t_pnr as a full scan, much faster.
Use --full_curve to evaluate every checkpoint (needed for risk-curve figures).

python scripts/03_pnr_scan.py --episodes "data/rollouts/*_n0.npz" --every 40 --K 5 --min_fail 3 --noise_std 0.05
"""

import argparse
import glob
import json
import os
import subprocess
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np  # noqa: E402

from pnr.pnr import find_pnr  # noqa: E402
from pnr.sim import CHUNK, Policy, make_task, max_steps, rollout  # noqa: E402

p = argparse.ArgumentParser()
p.add_argument("--episodes", default="data/rollouts/*.npz", help="glob of recorded episodes")
p.add_argument("--include_success", type=int, default=0, help="also scan this many successful episodes (controls)")
p.add_argument("--every", type=int, default=40)
p.add_argument("--K", type=int, default=5)
p.add_argument("--min_fail", type=int, default=3)
p.add_argument("--noise_std", type=float, default=0.05)
p.add_argument("--seed", type=int, default=0)
p.add_argument("--extra_steps", type=int, default=200,
               help="replays may run this many steps past 520, so late checkpoints are not doomed by the clock")
p.add_argument("--full_curve", action="store_true")
p.add_argument("--t_min", type=int, default=None, help="only scan checkpoints at or after this step (refinement)")
p.add_argument("--t_max", type=int, default=None, help="only scan checkpoints at or before this step (refinement)")
p.add_argument("--out", default="data/pnr")
args = p.parse_args()
assert args.every % CHUNK == 0, "--every must be a multiple of the action chunk (8)"

files = sorted(glob.glob(args.episodes))
eps = [(f, np.load(f, allow_pickle=True)) for f in files]
failed = [(f, e) for f, e in eps if not bool(e["success"])]
succ = [(f, e) for f, e in eps if bool(e["success"])][: args.include_success]
todo = failed + succ
print(f"{len(files)} episodes found: {len(failed)} failed, scanning {len(todo)}")
os.makedirs(args.out, exist_ok=True)
policy = Policy()

def claim(out_path):
    """Make sure only one job scans an episode, even with two job arrays on the same targets
    (galhp and preemptible reqp). Lock file = <out>.lock holding the Slurm job id. A job may take the
    lock if it is free, if it already holds it (a requeued job keeps its id, so it restarts cleanly), or
    if its owner is no longer in the queue (stale lock from a killed job)."""
    me = os.environ.get("SLURM_JOB_ID", f"pid{os.getpid()}")
    lock = out_path + ".lock"
    for _ in range(2):
        try:
            fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.write(fd, me.encode())
            os.close(fd)
            return True
        except FileExistsError:
            owner = open(lock).read().strip()
            if owner == me:
                return True
            alive = subprocess.run(["squeue", "-h", "-j", owner], capture_output=True, text=True)
            if alive.returncode == 0 and alive.stdout.strip():
                print(f"skip {os.path.basename(out_path)}: being scanned by job {owner}")
                return False
            if alive.returncode != 0 and "Invalid job id" not in alive.stderr:
                print(f"skip {os.path.basename(out_path)}: cannot check lock owner {owner} ({alive.stderr.strip()})")
                return False
            os.remove(lock)  # stale: owner is gone; try once more to create it
    return False


for f, ep in todo:
    eid = os.path.splitext(os.path.basename(f))[0]
    out_path = os.path.join(args.out, eid + ".json")
    if os.path.exists(out_path):
        print(f"skip {eid} (done)")
        continue
    if not claim(out_path):
        continue
    env, desc, _ = make_task(int(ep["task_id"]))
    q_steps = [int(s) for s in ep["query_steps"]]
    query_of = {s: i for i, s in enumerate(q_steps)}
    checkpoints = [s for s in q_steps if s % args.every == 0
                   and (args.t_min is None or s >= args.t_min) and (args.t_max is None or s <= args.t_max)]
    t_start = time.time()

    end_steps = {}  # policy step at which each replay ended (success step, or the horizon if it failed)

    def replay_outcomes(c):
        res = []
        end_steps[c] = []
        for k in range(args.K):
            rng = np.random.default_rng([args.seed, int(ep["task_id"]), int(ep["episode_idx"]), c, k])
            r = rollout(env, policy, desc, episode=ep, query=query_of[c], noise_std=args.noise_std,
                        rng=rng, record_states=False,
                        horizon=max_steps() + args.extra_steps)
            res.append(int(r.success))
            end_steps[c].append(int(r.t_end))
        return res

    results = {}
    if args.full_curve:
        for c in checkpoints:
            results[c] = replay_outcomes(c)
            print(f"  {eid} t={c}: successes {sum(results[c])}/{args.K}", flush=True)
    else:
        for c in reversed(checkpoints):
            results[c] = replay_outcomes(c)
            n_fail = args.K - sum(results[c])
            print(f"  {eid} t={c}: failures {n_fail}/{args.K}", flush=True)
            if n_fail < args.min_fail:
                break
    scanned = sorted(results)
    succ_matrix = np.array([results[c] for c in scanned])
    t_pnr = find_pnr(scanned, succ_matrix, args.min_fail)
    record = {
        "episode_id": eid, "task_id": int(ep["task_id"]), "episode_idx": int(ep["episode_idx"]),
        "description": str(ep["description"]), "recorded_success": bool(ep["success"]),
        "induced": bool(ep["induced"]), "t_end": int(ep["t_end"]),
        "checkpoints": scanned, "successes": succ_matrix.tolist(), "t_pnr": t_pnr,
        "end_steps": [end_steps[c] for c in scanned],
        "params": {"every": args.every, "K": args.K, "min_fail": args.min_fail,
                   "noise_std": args.noise_std, "seed": args.seed, "full_curve": args.full_curve,
                   "extra_steps": args.extra_steps, "t_min": args.t_min, "t_max": args.t_max},
        "minutes": round((time.time() - t_start) / 60, 1),
    }
    # Write to a temporary file and rename, so a job killed mid-write never leaves a half-written result.
    with open(out_path + ".tmp", "w") as fh:
        json.dump(record, fh, indent=1)
    os.replace(out_path + ".tmp", out_path)
    os.remove(out_path + ".lock")
    print(f"{eid}: t_pnr={t_pnr} (episode ended at {int(ep['t_end'])}) in {record['minutes']} min", flush=True)
    env.close()
