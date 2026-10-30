"""Join the held-out groups of a 06_train_predictor.py array run (--only_group, outputs DIR/g0, DIR/g1, ...) into
DIR/per_episode.json, DIR/failure_scores.json and DIR/all_scores.json, the files 13_report.py and 27_paper_metrics.py read.

python scripts/28_merge_groups.py --dir results/week3/baselines/unseen --groups 10
"""

import argparse
import json
import os

p = argparse.ArgumentParser()
p.add_argument("--dir", required=True)
p.add_argument("--groups", type=int, required=True)
args = p.parse_args()

rows = [r for g in range(args.groups) for r in json.load(open(os.path.join(args.dir, f"g{g}", "all_scores.json")))]
json.dump(rows, open(os.path.join(args.dir, "all_scores.json"), "w"))
json.dump([{k: v for k, v in r.items() if k not in ("labels", "scores", "steps", "risk", "ttp")} for r in rows],
          open(os.path.join(args.dir, "per_episode.json"), "w"), indent=1)
json.dump([r for r in rows if not r["success"]], open(os.path.join(args.dir, "failure_scores.json"), "w"))
print(f"{args.dir}: {len(rows)} rows from {args.groups} groups")
