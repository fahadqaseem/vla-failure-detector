"""Completeness check of the 20-replay ground truth (results/plan_nov22_gt20.md). First step of every job that reads it.

Every checkpoint every --every steps of every run in --targets must have <dir>/<eid>/c<step>.json with at least --K replays. Exit 0 if
so; otherwise print the missing / short files, append one ERROR line to --progress (once per --dir) and exit 1.

python scripts/70_gt20_complete.py --targets results/gt20/targets_oft.txt --dir data/gt20/oft
"""

import argparse
import json
import os
import sys
import time

import numpy as np

p = argparse.ArgumentParser()
p.add_argument("--targets", default="results/gt20/targets_oft.txt")
p.add_argument("--dir", default="data/gt20/oft")
p.add_argument("--every", type=int, default=8)
p.add_argument("--K", type=int, default=20)
p.add_argument("--progress", default="results/gt20/progress.md")
args = p.parse_args()

total, bad = 0, []
for line in open(args.targets):
    path_ep = line.strip()
    if not path_ep:
        continue
    eid = os.path.splitext(os.path.basename(path_ep))[0]
    for c in (int(s) for s in np.load(path_ep, allow_pickle=True)["query_steps"] if int(s) % args.every == 0):
        total += 1
        f = os.path.join(args.dir, eid, f"c{c:03d}.json")
        try:
            n = len(json.load(open(f))["replays"])
        except (OSError, ValueError, KeyError):
            n = 0
        if n < args.K:
            bad.append(f"{f} ({n} replays)")
if not bad:
    print(f"complete: {total} of {total} checkpoints in {args.dir} with {args.K} replays")
    sys.exit(0)
msg = (f"ERROR ({time.strftime('%Y-%m-%d %H:%M')}, job {os.environ.get('SLURM_JOB_ID', 'login')}): {args.dir} incomplete, "
       f"{len(bad)} of {total} checkpoints missing or with fewer than {args.K} replays (first: {', '.join(bad[:3])}). "
       "Jobs that read it stop here.")
print(msg, *bad[:50], sep="\n", file=sys.stderr)
old = open(args.progress).read() if os.path.exists(args.progress) else ""
if f"{args.dir} incomplete" not in old:
    with open(args.progress, "a") as fh:
        fh.write(f"\n- {msg}\n")
sys.exit(1)
