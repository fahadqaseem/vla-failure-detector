"""Pick natural failures from different tasks for full replay scans, with a fixed rule.

Rule (decided before seeing the data, Oct 18 2026): go through tasks in ascending task id; from each
task that has at least one natural failure, take the failure with the lowest initial-state index;
stop after n tasks.

python scripts/pick_failures.py --root data/natural --n 3            # print all picks
python scripts/pick_failures.py --root data/natural --n 3 --index 0  # print only pick 0 (for array jobs)
"""

import argparse
import csv
import glob
import os

p = argparse.ArgumentParser()
p.add_argument("--root", default="data/natural")
p.add_argument("--n", type=int, default=3)
p.add_argument("--index", type=int, default=None)
args = p.parse_args()

first_failure = {}  # task_id -> (episode_idx, path)
for index_path in sorted(glob.glob(os.path.join(args.root, "*", "index.csv"))):
    with open(index_path) as f:
        for row in csv.DictReader(f):
            if int(row["success"]) == 1 or int(row["induced"]) == 1:
                continue
            task, ep = int(row["task_id"]), int(row["episode_idx"])
            path = os.path.join(os.path.dirname(index_path), row["episode_id"] + ".npz")
            if task not in first_failure or ep < first_failure[task][0]:
                first_failure[task] = (ep, path)

picks = [first_failure[t][1] for t in sorted(first_failure)][: args.n]
if args.index is None:
    print("\n".join(picks))
elif args.index < len(picks):
    print(picks[args.index])
