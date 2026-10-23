"""Track 2 first checks for Pi0 / Pi0.5 (PNR_POLICY=pi0 or pi05, env ~/envs/pi), Oct 23 2026.

1. One episode (task 0, initial state 0), with timing per query.
2. Replay gate in the Pi setting: restore query 2 and replay with the episode's own flow seed: must reproduce the
   recording (max eef deviation over 80 steps).
3. Do replays with NEW flow seeds differ? Two replays from query 2 with seeds 1 and 2 (80 steps). If they are
   identical, the scans need added action noise (decision Oct 23).
Output: results/{policy}/checks.json and the episode in data/{policy}/checks/.

PNR_POLICY=pi0 python scripts/22_pi_checks.py
"""

import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pnr.sim_pi import CHECKPOINT, KIND, Policy, make_task, rollout, save_episode  # noqa: E402

out_dir = f"data/{KIND}/checks"
os.makedirs(out_dir, exist_ok=True)
os.makedirs(f"results/{KIND}", exist_ok=True)
t0 = time.time()
policy = Policy()
load_s = time.time() - t0
env, desc, inits = make_task(0)
t0 = time.time()
r = rollout(env, policy, desc, init_state=inits[0], rng=np.random.default_rng([0, 0, 0]))
ep_s = time.time() - t0
path = os.path.join(out_dir, "t00_e00_n0.npz")
save_episode(path, r, task_id=0, episode_idx=0, description=desc, init_state=inits[0], noise_std=0.0, seed=0)
ep = np.load(path, allow_pickle=True)
qi = 2
c = int(ep["query_steps"][qi])
rec = ep["eef"][c:c + 80]
same = rollout(env, policy, desc, episode=ep, query=qi, limit=80, record_states=False)
dev_same = float(np.abs(np.array(same.eef)[:len(rec)] - rec).max())
other = [rollout(env, policy, desc, episode=ep, query=qi, limit=80, record_states=False, rng=np.random.default_rng([s]))
         for s in (1, 2)]
n = min(len(other[0].eef), len(other[1].eef))
dev_new = float(np.abs(np.array(other[0].eef)[:n] - np.array(other[1].eef)[:n]).max())
res = {"policy": KIND, "checkpoint": CHECKPOINT, "episode_success": bool(r.success), "episode_steps": int(r.t_end),
       "queries": len(r.query_steps), "features_shape": list(np.array(r.features).shape),
       "model_load_s": round(load_s, 1), "episode_s": round(ep_s, 1), "s_per_query": round(ep_s / max(len(r.query_steps), 1), 3),
       "replay_same_seed_max_eef_dev_m": dev_same, "replay_gate_pass_10mm": dev_same <= 0.010,
       "two_new_seeds_max_eef_diff_m": dev_new, "new_seeds_differ_1mm": dev_new > 0.001}
json.dump(res, open(f"results/{KIND}/checks.json", "w"), indent=1)
print(json.dumps(res, indent=1))
