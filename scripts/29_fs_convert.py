"""Our episodes -> one cache file for FailureSpot (third_party/failurespot), Fahad Oct 30. Same labelled episodes and t_pnr
as T1all (read from its per_episode.json, so refined labels and pre-checks are not re-derived). One row per query:
features = features_mean (4096); action = first action of the query's chunk (action_horizon = execution_horizon = 1,
because OFT executes whole chunks, so chunks do not overlap and FailureSpot's overlap consistency is undefined; with H = K = 1
it falls back to the distance between successive first actions, 8 steps apart).

python scripts/29_fs_convert.py --out data/failurespot/trajectories.npz
"""

import argparse
import glob
import json
import os

import numpy as np

p = argparse.ArgumentParser()
p.add_argument("--labels", default="results/week2/T1all_unseen_conv/per_episode.json")
p.add_argument("--out", default="data/failurespot/trajectories.npz")
args = p.parse_args()

rows = {r["eid"]: r for r in json.load(open(args.labels)) if r["model"] == "progress"}
pats = ["data/natural/*/*.npz", "data/perturbed/task0[0145678]/*.npz"]
pats += [d + "/*.npz" for d in sorted(glob.glob("data/perturbed_v2/task*")) if os.path.exists(d + "/GATE_PASS")]
path = {os.path.splitext(os.path.basename(f))[0]: f for pat in pats for f in glob.glob(pat)}
missing = [e for e in rows if e not in path]
assert not missing, missing[:5]
print(f"{len(rows)} labelled episodes of {len(path)} files ({len(path) - len(rows)} unlabelled left out)", flush=True)
eids = sorted(rows)
feats, acts, offsets = [], [], [0]
for i, eid in enumerate(eids):
    ep = np.load(path[eid], allow_pickle=True)
    q = ep["query_steps"]
    feats.append(ep["features_mean"].astype(np.float32))
    a = ep["actions"]
    acts.append(a[np.minimum(np.arange(len(q)) * 8, len(a) - 1)].astype(np.float32))
    assert len(feats[-1]) == len(q)
    offsets.append(offsets[-1] + len(q))
    if i % 300 == 0:
        print(i, flush=True)
os.makedirs(os.path.dirname(args.out), exist_ok=True)
np.savez(args.out, features=np.concatenate(feats), actions=np.concatenate(acts), offsets=np.array(offsets), eids=np.array(eids),
         task=np.array([rows[e]["task"] for e in eids]), success=np.array([rows[e]["success"] for e in eids]),
         t_pnr=np.array([-1 if rows[e]["t_pnr"] is None else rows[e]["t_pnr"] for e in eids]),
         source=np.array([rows[e]["source"] for e in eids]))
print("saved", args.out, offsets[-1], "rows")
