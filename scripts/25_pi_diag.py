"""Track 2 diagnosis (Oct 28, after pi0 feasibility FAIL 42% vs 85.2%): success of our wrapper (pnr/sim_pi.py) on a
few tasks and initial states, with PNR_PI_STEPS actions per query. Same seeds as 01_collect (episode rng [seed, task,
init]). Output one json per run; 26_pi_diag_table.py puts it next to lerobot-eval.

PNR_POLICY=pi0 PNR_PI_STEPS=8 python scripts/25_pi_diag.py --tasks 0 8 --episodes 10 --out results/pi0/diag/ours_8.json
"""

import argparse
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pnr.sim_pi import CHUNK, KIND, Policy, make_task, rollout  # noqa: E402

p = argparse.ArgumentParser()
p.add_argument("--tasks", type=int, nargs="+", default=[0, 8])
p.add_argument("--episodes", type=int, default=10)
p.add_argument("--out", required=True)
args = p.parse_args()

policy = Policy()
res = {"policy": KIND, "setting": f"ours, {CHUNK} steps per query", "tasks": {}}
for task in args.tasks:
    env, desc, inits = make_task(task)
    succ = []
    for i in range(args.episodes):
        r = rollout(env, policy, desc, init_state=inits[i], rng=np.random.default_rng([0, task, i]), record_states=False)
        succ.append(bool(r.success))
        print(f"task {task} init {i}: {'success' if r.success else 'fail'} at {r.t_end}", flush=True)
    res["tasks"][str(task)] = succ
    env.close()
os.makedirs(os.path.dirname(args.out), exist_ok=True)
json.dump(res, open(args.out, "w"), indent=1)
