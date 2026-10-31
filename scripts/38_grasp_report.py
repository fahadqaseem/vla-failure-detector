"""Grasp-check report (Fahad, Oct 31): adds the gru_phys and gru_robot rows of the 50% regression run to the merged grasp run, so
13_report.py and 27_paper_metrics.py show them side by side.

python scripts/38_grasp_report.py --dir data/week3_grasp/unseen --ref data/week3_reg/thr50/unseen
"""

import argparse
import glob
import json
import os

p = argparse.ArgumentParser()
p.add_argument("--dir", required=True)
p.add_argument("--ref", required=True)
args = p.parse_args()
rows = json.load(open(os.path.join(args.dir, "all_scores.json")))
rows += [r for f in sorted(glob.glob(os.path.join(args.ref, "g*", "all_scores.json"))) for r in json.load(open(f)) if r["model"] in ("gru_phys", "gru_robot")]
json.dump(rows, open(os.path.join(args.dir, "all_scores.json"), "w"))
json.dump([{k: v for k, v in r.items() if k not in ("labels", "scores", "steps", "risk", "ttp")} for r in rows],
          open(os.path.join(args.dir, "per_episode.json"), "w"))
json.dump([r for r in rows if not r["success"]], open(os.path.join(args.dir, "failure_scores.json"), "w"))
print(len(rows))
