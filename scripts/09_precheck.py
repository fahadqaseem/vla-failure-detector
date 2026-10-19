"""Pre-check for new failures before a full scan (rule in CLAUDE.md, Fahad Oct 18 2026).

For each failed, non-induced episode: restore the checkpoint about 32 steps before the episode ended (the
last chunk boundary at or before t_end - 32) and run K = 4 replays with the scan settings (noise 0.05 on the
6 arm dims, extra_steps 200, same seeds as 03_pnr_scan.py). If at least --min_success (3, the tau 0.5 bar)
replays succeed, the failure is "recoverable (pre-check)" and gets no full scan: the last checkpoint is then
recoverable, so the t_pnr rule gives None. Otherwise its verdict is "scan".
One JSON per episode in --out; episodes that already have one are skipped.

python scripts/09_precheck.py --episodes "data/perturbed/task00/*.npz" --out data/perturbed/prechecks
"""

import argparse
import glob
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np  # noqa: E402

from pnr.sim import Policy, make_task, max_steps, rollout  # noqa: E402

p = argparse.ArgumentParser()
p.add_argument("--episodes", required=True)
p.add_argument("--out", required=True)
p.add_argument("--back", type=int, default=32, help="checkpoint = last chunk boundary at or before t_end - back")
p.add_argument("--K", type=int, default=4)
p.add_argument("--min_success", type=int, default=3)
p.add_argument("--noise_std", type=float, default=0.05)
p.add_argument("--extra_steps", type=int, default=200)
p.add_argument("--seed", type=int, default=0)
args = p.parse_args()

todo = []
for f in sorted(glob.glob(args.episodes)):
    ep = np.load(f, allow_pickle=True)
    eid = os.path.splitext(os.path.basename(f))[0]
    if not bool(ep["success"]) and not bool(ep["induced"]) and not os.path.exists(os.path.join(args.out, eid + ".json")):
        todo.append((eid, ep))
print(f"{len(todo)} failures to pre-check")
if not todo:
    sys.exit(0)
os.makedirs(args.out, exist_ok=True)
policy = Policy()

for eid, ep in todo:
    t_start = time.time()
    env, desc, _ = make_task(int(ep["task_id"]))
    q_steps = [int(s) for s in ep["query_steps"]]
    qi = max(i for i, s in enumerate(q_steps) if s <= int(ep["t_end"]) - args.back)
    c = q_steps[qi]
    successes = []
    for k in range(args.K):
        rng = np.random.default_rng([args.seed, int(ep["task_id"]), int(ep["episode_idx"]), c, k])
        r = rollout(env, policy, desc, start_state=ep["query_states"][qi], start_gripper=ep["query_grippers"][qi],
                    t0=c, noise_std=args.noise_std, rng=rng, record_states=False,
                    horizon=max_steps() + args.extra_steps)
        successes.append(int(r.success))
    verdict = "recoverable (pre-check)" if sum(successes) >= args.min_success else "scan"
    record = {"episode_id": eid, "task_id": int(ep["task_id"]), "episode_idx": int(ep["episode_idx"]),
              "t_end": int(ep["t_end"]), "checkpoint": c, "successes": successes, "verdict": verdict,
              "params": {k: getattr(args, k) for k in ["back", "K", "min_success", "noise_std", "extra_steps", "seed"]},
              "minutes": round((time.time() - t_start) / 60, 1)}
    path = os.path.join(args.out, eid + ".json")
    with open(path + ".tmp", "w") as fh:
        json.dump(record, fh, indent=1)
    os.replace(path + ".tmp", path)
    print(f"{eid}: checkpoint {c} of {int(ep['t_end'])}, successes {successes} -> {verdict} ({record['minutes']} min)", flush=True)
    env.close()
