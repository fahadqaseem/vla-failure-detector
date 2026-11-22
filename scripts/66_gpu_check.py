"""GPU type check for the 20-replay ground truth (results/plan_nov22_gt20.md, amendment Nov 22).

Reruns, on the GPU of this job, every replay of some finished pilot checkpoints (data/gt20_pilot/<eid>/c<step>.json, made on L40S; the
reused seed 0 / seed 1 replays come from the October L40S scans) with the same seeds, and compares outcome and end step replay by replay.
Also reports seconds per replay on this GPU. Writes one JSON per GPU type.

python scripts/66_gpu_check.py --checkpoints data/gt20_pilot/t01_e07_p0_s1/c000.json --out results/gt20/gpu_check
"""

import argparse
import json
import os
import subprocess
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np  # noqa: E402

from pnr.policy import Policy, make_task, max_steps, rollout  # noqa: E402

p = argparse.ArgumentParser()
p.add_argument("--checkpoints", nargs="+", required=True)
p.add_argument("--episodes_root", default="data/perturbed_v2")
p.add_argument("--out", default="results/gt20/gpu_check")
args = p.parse_args()
gpu = subprocess.run(["nvidia-smi", "--query-gpu=name", "--format=csv,noheader"], capture_output=True, text=True).stdout.strip().splitlines()[0]
policy = Policy()
res = []
for path in args.checkpoints:
    c = json.load(open(path))
    eid, task = c["episode_id"], c["task_id"]
    ep = np.load(os.path.join(args.episodes_root, f"task{task:02d}", eid + ".npz"), allow_pickle=True)
    q = [int(s) for s in ep["query_steps"]].index(c["checkpoint"])
    env, desc, _ = make_task(task)
    for r in c["replays"]:
        rng = np.random.default_rng([r["seed"], task, int(ep["episode_idx"]), c["checkpoint"], r["k"]])
        t0 = time.time()
        out = rollout(env, policy, desc, episode=ep, query=q, noise_std=c["params"]["noise_std"], rng=rng, record_states=False,
                      horizon=max_steps() + c["params"]["extra_steps"])
        res.append(dict(eid=eid, checkpoint=c["checkpoint"], seed=r["seed"], k=r["k"], l40s_success=r["success"],
                        l40s_end=r["end_step"], success=int(out.success), end_step=int(out.t_end), seconds=round(time.time() - t0, 2)))
        print(res[-1], flush=True)
    env.close()
same_out = sum(x["success"] == x["l40s_success"] for x in res)
same_end = sum(x["end_step"] == x["l40s_end"] for x in res)
summary = dict(gpu=gpu, node=os.uname().nodename, job=os.environ.get("SLURM_JOB_ID"), replays=len(res), same_outcome=same_out,
               same_end_step=same_end, l40s_successes=sum(x["l40s_success"] for x in res), successes=sum(x["success"] for x in res),
               sec_fail=float(np.mean([x["seconds"] for x in res if not x["success"]] or [np.nan])),
               sec_succ=float(np.mean([x["seconds"] for x in res if x["success"]] or [np.nan])))
print(summary)
os.makedirs(args.out, exist_ok=True)
json.dump(dict(summary=summary, replays=res), open(os.path.join(args.out, gpu.replace(" ", "_") + ".json"), "w"), indent=1)
