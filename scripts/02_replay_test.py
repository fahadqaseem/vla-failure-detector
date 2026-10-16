"""Determinism check. Must pass before any PNR scan.

Restores a saved chunk-boundary state, replays the policy with NO noise, and compares the end-effector
trajectory (and, with --full, the final outcome) with the recorded episode.

python scripts/02_replay_test.py --episode data/rollouts/t00_e00_n0.npz --steps 80 --full
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np  # noqa: E402

from pnr.sim import Policy, make_task, rollout  # noqa: E402

p = argparse.ArgumentParser()
p.add_argument("--episode", required=True)
p.add_argument("--query", type=int, default=-1, help="which recorded query to restore (default: middle)")
p.add_argument("--steps", type=int, default=80)
p.add_argument("--full", action="store_true", help="also replay to the end and compare outcome")
p.add_argument("--tol_m", type=float, default=0.005, help="max allowed eef deviation in metres")
args = p.parse_args()

ep = np.load(args.episode, allow_pickle=True)
q_steps, q_states, eef = ep["query_steps"], ep["query_states"], ep["eef"]
qi = len(q_steps) // 2 if args.query < 0 else args.query
t0 = int(q_steps[qi])
env, desc, _ = make_task(int(ep["task_id"]))
policy = Policy()

# 1) State restore is exact?
env.reset()
env.set_init_state(q_states[qi])
state_err = float(np.abs(env.get_sim_state() - q_states[qi]).max())
print(f"restore query {qi} (policy step {t0}): max |state diff| = {state_err:.2e}")

# 2) Short replay matches the recorded trajectory?
r = rollout(env, policy, desc, start_state=q_states[qi], t0=t0, limit=args.steps, record_states=False)
n = min(len(r.eef), len(eef) - t0)
dev = np.linalg.norm(np.stack(r.eef[:n]) - eef[t0:t0 + n], axis=1)
print(f"replayed {n} steps: eef deviation max {dev.max() * 1000:.2f} mm, mean {dev.mean() * 1000:.2f} mm")
ok = dev.max() <= args.tol_m

# 3) Full replay reaches the same outcome?
if args.full:
    rf = rollout(env, policy, desc, start_state=q_states[qi], t0=t0, record_states=False)
    same = bool(rf.success) == bool(ep["success"])
    print(f"full replay: success={rf.success} (recorded {bool(ep['success'])}), steps {rf.t_end} (recorded {int(ep['t_end'])})")
    ok = ok and same

print("PASS" if ok else "FAIL: fix determinism before running PNR scans (see CLAUDE.md)")
sys.exit(0 if ok else 1)
