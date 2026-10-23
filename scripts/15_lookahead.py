"""Phase B look-ahead (Fahad, Oct 23, docs/PLAN_week2.md). UPPER BOUND, NOT A DETECTOR: it uses the simulator
at test time to imagine the near future.

For one episode: at every --every (16) steps, restore the query (restore_query, as the scans) and run --K (4)
futures of --horizon (48) policy steps with action noise --noise_std (0.05). Saved per checkpoint and future:
  no_move   eef moved less than --move_m (1 cm) between the first and the last step of the future
  success   the future solved the task
  x_future  the predictor's input row at the future's last query (features_mean, its action chunk, eef, gripper),
            scored later by the leave-one-task-out mlp (06_train_predictor.py --lookahead)
One npz per episode in --out; episodes that already have one are skipped.

--write_targets: write the episode list instead (101 labelled failures of --pred, 10 natural successes per
task and 50 perturbed successes spread over the tasks, lowest initial-state index first).

python scripts/15_lookahead.py --write_targets results/week2/lookahead/targets.txt
python scripts/15_lookahead.py --targets results/week2/lookahead/targets.txt --lines 0 10 --out data/week2_lookahead
"""

import argparse
import glob
import json
import os
import sys
import time

import numpy as np

p = argparse.ArgumentParser()
p.add_argument("--targets", default="results/week2/lookahead/targets.txt")
p.add_argument("--lines", type=int, nargs=2, default=[0, 10], help="first line and number of lines to run")
p.add_argument("--out", default="data/week2_lookahead")
p.add_argument("--every", type=int, default=16)
p.add_argument("--K", type=int, default=4)
p.add_argument("--horizon", type=int, default=48)
p.add_argument("--noise_std", type=float, default=0.05)
p.add_argument("--move_m", type=float, default=0.01)
p.add_argument("--seed", type=int, default=100, help="differs from the scan seeds (0, 1)")
p.add_argument("--write_targets", default=None)
p.add_argument("--pred", default="results/predictor_with_perturbed")
args = p.parse_args()

if args.write_targets:
    rows = [r for r in json.load(open(os.path.join(args.pred, "per_episode.json"))) if r["model"] == "progress"]
    files = {os.path.splitext(os.path.basename(f))[0]: f
             for pat in ["data/natural/*/*.npz", "data/perturbed/*/*.npz"] for f in glob.glob(pat)}
    idx = lambda r: int(r["eid"].split("_")[1][1:])  # noqa: E731  initial-state index from tXX_eYY_...
    fails = sorted((r for r in rows if not r["success"]), key=lambda r: r["eid"])
    succ_nat = [r for t in range(10) for r in sorted((r for r in rows if r["success"] and r["source"] == "natural"
                                                      and r["task"] == t), key=idx)[:10]] if "source" in rows[0] else \
        [r for t in range(10) for r in sorted((r for r in rows if r["success"] and r["eid"].endswith("_n0")
                                               and r["task"] == t), key=idx)[:10]]
    pert = [r for r in rows if r["success"] and "_p" in r["eid"]]
    tasks = sorted({r["task"] for r in pert})
    by_task = {t: sorted((r for r in pert if r["task"] == t), key=idx) for t in tasks}
    succ_pert = []
    i = 0
    while len(succ_pert) < 50:  # round robin over tasks: 7 or 8 per task
        t = tasks[i % len(tasks)]
        j = i // len(tasks)
        if j < len(by_task[t]):
            succ_pert.append(by_task[t][j])
        i += 1
    chosen = fails + succ_nat + succ_pert
    os.makedirs(os.path.dirname(args.write_targets), exist_ok=True)
    open(args.write_targets, "w").write("".join(files[r["eid"]] + "\n" for r in chosen))
    print(f"{len(fails)} failures, {len(succ_nat)} natural successes, {len(succ_pert)} perturbed successes "
          f"-> {args.write_targets}")
    sys.exit(0)

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pnr.sim import CHUNK, Policy, make_task, rollout  # noqa: E402

paths = [line.strip() for line in open(args.targets) if line.strip()][args.lines[0]:args.lines[0] + args.lines[1]]
todo = [f for f in paths if not os.path.exists(os.path.join(args.out, os.path.splitext(os.path.basename(f))[0] + ".npz"))]
print(f"{len(todo)} of {len(paths)} episodes to run", flush=True)
if not todo:
    sys.exit(0)
os.makedirs(args.out, exist_ok=True)
policy = Policy()
for f in todo:
    t0 = time.time()
    ep = np.load(f, allow_pickle=True)
    eid = os.path.splitext(os.path.basename(f))[0]
    env, desc, _ = make_task(int(ep["task_id"]))
    q_steps = [int(s) for s in ep["query_steps"]]
    cks = [(i, s) for i, s in enumerate(q_steps) if s % args.every == 0]
    no_move = np.zeros((len(cks), args.K), bool)
    success = np.zeros((len(cks), args.K), bool)
    x_future = []
    for j, (qi, c) in enumerate(cks):
        rows = []
        for k in range(args.K):
            rng = np.random.default_rng([args.seed, int(ep["task_id"]), int(ep["episode_idx"]), c, k])
            r = rollout(env, policy, desc, episode=ep, query=qi, noise_std=args.noise_std, rng=rng,
                        record_states=True, limit=args.horizon)
            eef = np.array(r.eef)
            no_move[j, k] = np.linalg.norm(eef[-1] - eef[0]) < args.move_m
            success[j, k] = r.success
            last = len(r.query_steps) - 1
            rel = r.query_steps[last] - c  # step of the last query, relative to the checkpoint
            chunk = np.array(r.actions[rel:rel + CHUNK])
            chunk = np.pad(chunk, ((0, CHUNK - len(chunk)), (0, 0))).reshape(-1)
            rows.append(np.concatenate([r.features[last].astype(np.float32).mean(0), chunk, eef[rel],
                                        r.query_grippers[last]]).astype(np.float32))
        x_future.append(rows)
    np.savez_compressed(os.path.join(args.out, eid + ".npz"), steps=np.array([c for _, c in cks]), no_move=no_move,
                        success=success, x_future=np.array(x_future, np.float16),
                        params=json.dumps({k: getattr(args, k) for k in ["every", "K", "horizon", "noise_std", "move_m", "seed"]}))
    env.close()
    print(f"{eid}: {len(cks)} checkpoints, no-move {no_move.mean():.2f}, any future succeeds at "
          f"{int(success.any(1).sum())} checkpoints, {time.time() - t0:.0f}s", flush=True)
