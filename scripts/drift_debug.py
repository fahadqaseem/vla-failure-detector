"""Debug a replay that drifts from its recording (Oct 19 2026; first used on t01_e41_n0 q32 as data/drift_dbg.py).

For each episode:query pair, run 2 replays from restore_query (no noise) for --limit steps and print the first
step where the actions differ from the recording, the size of that difference, the sim-state difference at the
next queries, and whether the 2 replays agree with each other (policy and GPU determinism).

python scripts/drift_debug.py data/perturbed/task03/t03_e00_p0.npz:1 --limit 240
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import numpy as np  # noqa: E402
from pnr.sim import Policy, make_task, rollout  # noqa: E402

p = argparse.ArgumentParser()
p.add_argument("pairs", nargs="+", help="episode.npz:query")
p.add_argument("--limit", type=int, default=120, help="steps per replay")
args = p.parse_args()

policy = Policy()
for path, qi in [(a.split(":")[0], int(a.split(":")[1])) for a in args.pairs]:
    ep = np.load(path, allow_pickle=True)
    env, desc, _ = make_task(int(ep["task_id"]))
    t0 = int(ep["query_steps"][qi])
    runs = [rollout(env, policy, desc, episode=ep, query=qi, limit=args.limit) for _ in range(2)]
    for i, r in enumerate(runs):
        a = np.stack(r.actions); rec = ep["actions"][t0:t0 + len(a)]
        d = np.abs(a - rec).max(axis=1)
        first = int(np.argmax(d > 0)) if (d > 0).any() else None
        print(f"{path} q{qi} run {i}: first action diff at step {None if first is None else t0 + first}, "
              f"diff there {0 if first is None else d[first]:.3g}, max {d.max():.3g}; "
              f"state diff at later queries: " + ", ".join(f"{s}:{np.abs(st - ep['query_states'][list(ep['query_steps']).index(s)]).max():.1e}"
                                                            for s, st in list(zip(r.query_steps, r.query_states))[:6] if s in list(ep['query_steps'])), flush=True)
    a0, a1 = np.stack(runs[0].actions), np.stack(runs[1].actions)
    n = min(len(a0), len(a1))
    print(f"   run 0 vs run 1 action max diff {np.abs(a0[:n] - a1[:n]).max():.3g}")
    env.close()
