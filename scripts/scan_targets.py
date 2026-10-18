"""Write the fixed list of episodes to label with full replay scans (one line per Slurm array task).

Rule (decided Oct 18 2026, before any of these scans ran):
  - every natural failure, in task order, then initial-state order;
  - then n_success successful episodes per task: the ones with the lowest initial-state index.
Failures come first so that they finish first.

python scripts/scan_targets.py --root data/natural --n_success 2 --out results/full_scans/targets.txt
"""

import argparse
import csv
import glob
import os

p = argparse.ArgumentParser()
p.add_argument("--root", default="data/natural")
p.add_argument("--n_success", type=int, default=2, help="successful episodes per task")
p.add_argument("--out", default="results/full_scans/targets.txt")
args = p.parse_args()

failures, successes = [], []
for index_path in sorted(glob.glob(os.path.join(args.root, "*", "index.csv"))):
    with open(index_path) as f:
        rows = [r for r in csv.DictReader(f) if int(r["induced"]) == 0]
    rows.sort(key=lambda r: int(r["episode_idx"]))
    path = lambda r: os.path.join(os.path.dirname(index_path), r["episode_id"] + ".npz")  # noqa: E731
    failures += [path(r) for r in rows if int(r["success"]) == 0]
    successes += [path(r) for r in rows if int(r["success"]) == 1][: args.n_success]

os.makedirs(os.path.dirname(args.out), exist_ok=True)
with open(args.out, "w") as f:
    f.write("\n".join(failures + successes) + "\n")
print(f"{len(failures)} failures + {len(successes)} successes = {len(failures) + len(successes)} lines -> {args.out}")
