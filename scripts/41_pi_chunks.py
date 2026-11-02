"""All 50 predicted actions of every Pi0.5 query (Fahad, Oct 31; FailureSpot needs them, episodes save only the 8 executed ones). Replays one
task's episodes with the recorded actions and asks the policy again at each query with the query's own flow seed, which reproduces the chunk. The first
8 are checked against the recording. One file per episode in data/{policy}/chunks: chunks (n_queries, 50, 7).

PNR_POLICY=pi05 python scripts/41_pi_chunks.py --task 0
"""

import argparse
import glob
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pnr.sim_pi import KIND, Policy, make_task, query_seed, restore_query  # noqa: E402

p = argparse.ArgumentParser()
p.add_argument("--task", type=int, required=True)
p.add_argument("--limit", type=int, default=None, help="first episodes only (test)")
args = p.parse_args()
files = sorted(f for k in ("natural", "perturbed", "perturbed_l2") for f in glob.glob(f"data/{KIND}/{k}/task{args.task:02d}*/*.npz") if ".tmp." not in f)[:args.limit]
os.makedirs(f"data/{KIND}/chunks", exist_ok=True)
policy = Policy()
policy.keep_full = True
env, desc, _ = make_task(args.task)
dev = []
for n, f in enumerate(files):
    eid = os.path.splitext(os.path.basename(f))[0]
    out = f"data/{KIND}/chunks/{eid}.npz"
    if os.path.exists(out):
        continue
    ep = dict(np.load(f, allow_pickle=True))
    q = [int(s) for s in ep["query_steps"]]
    raw = restore_query(env, ep, 0)
    chunks = []
    for s in q:
        policy.act(env.lerobot._format_raw_obs(raw), desc, query_seed(int(ep["flow_seed"]), s))
        chunks.append(policy.last_full)
        rec = ep["actions"][s:s + 8]
        dev.append(float(np.abs(policy.last_full[:len(rec)] - rec).max()))
        for a in rec:
            raw, _, _, _ = env.step(a.tolist())
    np.savez_compressed(out + ".tmp.npz", chunks=np.stack(chunks).astype(np.float32))
    os.replace(out + ".tmp.npz", out)
    print(f"{n + 1}/{len(files)} {eid}: max action difference {max(dev[-len(q):]):.4f}", flush=True)
os.makedirs(f"results/{KIND}/chunks", exist_ok=True)
json.dump({"task": args.task, "queries": len(dev), "median_max_diff": float(np.median(dev)) if dev else None, "max_diff": max(dev) if dev else None},
          open(f"results/{KIND}/chunks/task{args.task}.json", "w"))
