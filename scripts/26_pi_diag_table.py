"""Table of 25_pi_diag.py runs and lerobot-eval (eval_info.json) for the pi0 diagnosis (Oct 28): success per task.

python scripts/26_pi_diag_table.py --dir results/pi0/diag --out results/pi0/diag.md
"""

import argparse
import glob
import json
import os

p = argparse.ArgumentParser()
p.add_argument("--dir", required=True)
p.add_argument("--out", required=True)
args = p.parse_args()

rows = []
for f in sorted(glob.glob(os.path.join(args.dir, "lerobot_eval*/eval_info.json"))):
    info = json.load(open(f))
    tasks = {str(t["task_id"]): [bool(s) for s in t["metrics"]["successes"]] for t in info["per_task"]}
    rows.append(("lerobot-eval, default settings (50 steps per query, 360 px)", tasks))
for f in sorted(glob.glob(os.path.join(args.dir, "ours_*.json")), key=lambda f: int(f.split("_")[-1][:-5])):
    d = json.load(open(f))
    rows.append((d["setting"], d["tasks"]))
ids = sorted({t for _, tasks in rows for t in tasks}, key=int)
lines = ["# pi0 diagnosis: success on tasks " + ", ".join(ids) + " (initial states 0 to 9)", "",
         "| setting | " + " | ".join(f"task {t}" for t in ids) + " | overall |", "|---" * (len(ids) + 2) + "|"]
for name, tasks in rows:
    cells = [f"{sum(tasks[t])}/{len(tasks[t])}" if t in tasks else "-" for t in ids]
    s = sum(sum(v) for v in tasks.values()); n = sum(len(v) for v in tasks.values())
    lines.append(f"| {name} | " + " | ".join(cells) + f" | {s}/{n} = {100 * s / n:.0f}% |")
open(args.out, "w").write("\n".join(lines) + "\n")
print("\n".join(lines))
