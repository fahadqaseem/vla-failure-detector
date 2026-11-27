"""20-replay ground truth, full run (results/plan_nov22_gt20.md, amendment Nov 22). One worker = one GPU job.

Every worker walks the same list of failed runs (--targets, one episode .npz per line) and, checkpoint by checkpoint (every --every
steps), claims a lock (<out>/<eid>/c<step>.json.lock holding the Slurm job id), brings that checkpoint to --K replays and writes
c<step>.json (temp file + rename). Workers on different GPU types share the work; a requeued or killed worker leaves a stale lock that
the next worker takes over (its owner is no longer in the queue). Same replay rule as 03_pnr_scan.py / 63_gt20_scan.py:
rng = default_rng([seed, task, episode_idx, checkpoint, k]); new replays use --seed (20; 0, 1 and 100 are already used).

Existing replays reused at a checkpoint, when settings match (noise_std, extra_steps, restore_query, deterministic):
  a pilot file (--pilot/<eid>/c<step>.json, complete list) if present, else the K 4 scan (seed 0) plus refinement replays (seed 1).
Every replay records the GPU it ran on ("gpu"; reused ones keep "L40S (earlier scan)" unless the pilot file says otherwise).

python scripts/67_gt20_worker.py --targets results/gt20/targets_oft.txt --scans "data/full_scans/*.json" ... --out data/gt20/oft
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

from pnr.policy import CHUNK, DETERMINISTIC, REPLAY_START, Policy, make_task, max_steps, rollout  # noqa: E402

p = argparse.ArgumentParser()
p.add_argument("--targets", required=True)
p.add_argument("--scans", nargs="+", required=True, help="globs of existing scan JSONs")
p.add_argument("--refine", default=None)
p.add_argument("--pilot", default=None)
p.add_argument("--every", type=int, default=8)
p.add_argument("--K", type=int, default=20)
p.add_argument("--seed", type=int, default=20)
p.add_argument("--noise_std", type=float, required=True, help="OFT 0.05; Pi0.5 0 (its own flow sampling), as the existing scans")
p.add_argument("--extra_steps", type=int, default=200)
p.add_argument("--out", required=True)
args = p.parse_args()
assert args.every % CHUNK == 0
SAME = dict(noise_std=args.noise_std, extra_steps=args.extra_steps, replay_start=REPLAY_START, deterministic=DETERMINISTIC)
ME = os.environ.get("SLURM_JOB_ID", f"pid{os.getpid()}")
GPU = subprocess.run(["nvidia-smi", "--query-gpu=name", "--format=csv,noheader"], capture_output=True, text=True).stdout.strip()
GPU = GPU.splitlines()[0] if GPU else "unknown"
print("worker", ME, "on", os.uname().nodename, GPU, flush=True)

scan_of = {}
for f in [f for g in args.scans for f in glob.glob(g)]:
    s = json.load(open(f))
    if "successes" in s and all(s["params"].get(k) == v for k, v in SAME.items()):
        scan_of[s["episode_id"]] = [f]
if args.refine:
    for f in glob.glob(os.path.join(args.refine, "*.json")):
        r = json.load(open(f))
        if r["episode_id"] in scan_of and all(r["params"].get(k) == v for k, v in SAME.items()):
            scan_of[r["episode_id"]].append(f)


def claim(path):
    """Lock = <path>.lock with the owner's job id, written atomically (hard link of a temp file, Nov 23 fix).
    Free, own (a requeued job keeps its id) -> take it. Empty or unreadable lock (old-code workers create the file first and write the
    id after) -> held, unless older than 10 minutes. A lock with a job id is stale only if squeue says that id is not in the queue."""
    lock = path + ".lock"
    for _ in range(2):
        tmp = lock + ".tmp." + ME
        with open(tmp, "w") as fh:
            fh.write(ME)
        try:
            os.link(tmp, lock)
            got = True
        except FileExistsError:
            got = False
        os.remove(tmp)
        if got:
            return True
        try:
            owner = open(lock).read().strip()
            age = time.time() - os.path.getmtime(lock)
        except FileNotFoundError:
            continue  # released meanwhile: try again
        except OSError:
            return False  # unreadable: held
        if owner == ME:
            return True
        if not owner:
            if age < 600:
                return False  # empty and young: an old-code worker is writing its id
        else:
            q = subprocess.run(["squeue", "-h", "-j", owner], capture_output=True, text=True)
            if q.returncode == 0 and q.stdout.strip():
                return False  # owner in the queue
            if q.returncode != 0 and "Invalid job id" not in q.stderr:
                return False  # cannot tell: leave it
        try:
            os.remove(lock)
        except FileNotFoundError:
            pass
    return False


def complete(path):
    """Checkpoint file present, readable and with at least K replays."""
    try:
        return len(json.load(open(path))["replays"]) >= args.K
    except (OSError, ValueError, KeyError):
        return False


def release(path):
    """Remove the lock only if it is ours."""
    try:
        if open(path + ".lock").read().strip() == ME:
            os.remove(path + ".lock")
    except FileNotFoundError:
        pass


policy = Policy()
envs = {}
# Passes over the run list until no checkpoint is missing (Nov 27, second pass): a checkpoint skipped because another job held its
# lock is looked at again; if that job died, its lock is stale and taken over (claim).
n_pass = 0
while True:
    n_pass += 1
    waiting = 0
    for line in open(args.targets):
        path_ep = line.strip()
        if not path_ep:
            continue
        eid = os.path.splitext(os.path.basename(path_ep))[0]
        out_dir = os.path.join(args.out, eid)
        os.makedirs(out_dir, exist_ok=True)
        ep = np.load(path_ep, allow_pickle=True)
        task, idx = int(ep["task_id"]), int(ep["episode_idx"])
        q_steps = [int(s) for s in ep["query_steps"]]
        todo = [c for c in q_steps if c % args.every == 0 and not complete(os.path.join(out_dir, f"c{c:03d}.json"))]
        if not todo:
            continue
        assert eid in scan_of, f"{eid}: no scan with matching settings"
        reuse = {}
        for f in scan_of[eid]:
            s = json.load(open(f))
            for c, succ, ends in zip(s["checkpoints"], s["successes"], s["end_steps"]):
                reuse.setdefault(int(c), []).extend(dict(seed=s["params"]["seed"], k=k, success=int(v), end_step=int(e), seconds=None,
                                                         source="reused", gpu="L40S (earlier scan)")
                                                    for k, (v, e) in enumerate(zip(succ, ends)))
        for c in todo:
            path = os.path.join(out_dir, f"c{c:03d}.json")
            if complete(path):
                continue
            if not claim(path):
                waiting += 1  # held by a live job (or cannot tell): look again on the next pass
                continue
            if complete(path):  # written by another worker between the check and the claim
                release(path)
                continue
            pilot = os.path.join(args.pilot, eid, f"c{c:03d}.json") if args.pilot else None
            if pilot and os.path.exists(pilot):
                pj = json.load(open(pilot))
                old = [dict(r, source="reused", gpu="NVIDIA L40S (pilot)" if r["source"] == "new" else "L40S (earlier scan)")
                       for r in pj["replays"]]  # the pilot ran on L40S only (galhp)
            else:
                old = reuse.get(c, [])
            old = old[: args.K]
            old_keys = {(r["seed"], r["k"]) for r in old}
            new_keys = [(args.seed, k) for k in range(args.K) if (args.seed, k) not in old_keys][: args.K - len(old)]
            assert not old_keys & set(new_keys)
            first = lambda s, k: np.random.default_rng([s, task, idx, c, k]).normal(0, 1, 6)  # noqa: E731
            for a in new_keys:
                fa = first(*a)
                assert not any(np.allclose(fa, first(*b)) for b in old_keys), (eid, c, a)
            if task not in envs:
                envs[task] = make_task(task)
            env, desc, _ = envs[task]
            replays = list(old)
            for s, k in new_keys:
                t0 = time.time()
                r = rollout(env, policy, desc, episode=ep, query=q_steps.index(c), noise_std=args.noise_std,
                            rng=np.random.default_rng([s, task, idx, c, k]), record_states=False, horizon=max_steps() + args.extra_steps)
                replays.append(dict(seed=s, k=k, success=int(r.success), end_step=int(r.t_end), seconds=round(time.time() - t0, 2),
                                    source="new", gpu=GPU))
            rec = dict(episode_id=eid, task_id=task, episode_idx=idx, checkpoint=c, t_end=int(ep["t_end"]), replays=replays,
                       params=dict(SAME, every=args.every, K=args.K, new_seed=args.seed, node=os.uname().nodename, job=ME, gpu=GPU))
            if complete(path):  # another worker wrote it meanwhile (same seeds): keep the first copy
                release(path)
                print(f"{eid} t={c}: already written by another worker, skipped", flush=True)
                continue
            with open(path + ".tmp." + ME, "w") as fh:
                json.dump(rec, fh, indent=1)
            os.replace(path + ".tmp." + ME, path)
            release(path)
            print(f"{eid} t={c}: {len(old)} reused + {len(new_keys)} new, successes {sum(r['success'] for r in replays)}/{len(replays)}",
                  flush=True)
    if waiting == 0:
        break
    print(f"worker {ME}: pass {n_pass} done, {waiting} checkpoints held by other jobs, next pass in 120 s", flush=True)
    time.sleep(120)
print("worker", ME, "found nothing left to claim")
