"""Inputs of the micro_phys model (pnr_probe, Oct 29 2026): Track 1 physical signals (33) + the 3 micro-event counts of
precursor_features.py (contact flicker, gripper close-reopen, jerk spikes over the last 8 queries), one file per episode
in the 20_physical_signals.py format (read by 06 with --phys). The micro counts are the cross-fitted ones of the split.

python pnr_probe/micro_phys/combine.py --micro pnr_probe/data/unseen/micro --out pnr_probe/data/micro_phys/unseen
"""

import argparse
import glob
import os

import numpy as np

p = argparse.ArgumentParser()
p.add_argument("--phys", default=os.path.expanduser("~/vla-failure-detector/data/physical"))
p.add_argument("--micro", required=True)
p.add_argument("--out", required=True)
args = p.parse_args()

os.makedirs(args.out, exist_ok=True)
files = sorted(glob.glob(os.path.join(args.micro, "*.npz")))
for f in files:
    eid = os.path.basename(f)
    ph, mi = np.load(os.path.join(args.phys, eid)), np.load(f)
    assert (ph["query_steps"] == mi["query_steps"]).all(), eid
    np.savez(os.path.join(args.out, eid), x=np.concatenate([ph["x"], mi["x"]], 1).astype(np.float32),
             names=np.array(list(ph["names"]) + list(mi["names"])), query_steps=ph["query_steps"])
print(f"done: {len(files)} episodes -> {args.out}, names {list(ph['names'])[-2:]} + {list(mi['names'])}")
