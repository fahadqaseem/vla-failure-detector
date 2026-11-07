"""Task-level robustness (Fahad, Nov 7, item 1): per held-out task, timely alarms and false alarms of progress, gru_phys_ttp (seeds 0 to 4 and
the seed ensemble) and the OR rules, both policies, all rules, unseen tasks, budgets 2.5% and 5%. The model-minus-progress difference is
bootstrapped over held-out tasks (10000 draws, seed 0: resample the 10 tasks with replacement, sum the per-task differences), and the tasks
where the model is better / worse / equal on timely alarms are counted. 70% is the main rule.

python scripts/51_tasklevel.py --out results/tasklevel
"""

import argparse
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from audit_lib import KEYS, POLS, RULES, alarms, caught, main_models, timed  # noqa: E402

p = argparse.ArgumentParser()
p.add_argument("--out", default="results/tasklevel")
args = p.parse_args()


def per_task(rows, key):
    out = {}
    for t in sorted({r["task"] for r in rows}):
        mine = [r for r in rows if r["task"] == t]
        tf, su = [r for r in mine if timed(r)], [r for r in mine if r["success"]]
        out[t] = dict(timely=sum(caught(r, key) for r in tf), n=len(tf), fa=sum(r["alarms"][key] is not None for r in su), ns=len(su))
    return out


summ = ["| policy | rule | budget | model | timely (vs progress) | bootstrap over tasks (95%) | tasks better / worse / equal | "
        "false alarms (vs progress) | bootstrap over tasks (95%) |", "|---|---|---|---|---|---|---|---|---|"]
detail = ["| policy | rule | budget | task | timed failures | successes | " + " | ".join(
    f"{m} timely / FA" for m in ("progress", "gru_phys_ttp s0", "gru_phys_ttp_ens", "or_progress_ttp s0", "or_progress_ens")) + " |",
          "|---|---|---|---|---|---|" + "---|" * 5]
missing = []
for pol in POLS:
    for thr in RULES:
        for key in KEYS:
            pt = per_task(alarms(pol, thr, "progress"), key)
            tasks = sorted(pt)
            draws = np.random.default_rng(0).integers(0, len(tasks), (10000, len(tasks)))
            got = {"progress": pt}
            for label, model, seed in main_models():
                if model == "progress":
                    continue
                try:
                    mt = per_task(alarms(pol, thr, model, seed), key)
                except FileNotFoundError as e:
                    missing.append(f"{pol} {thr} {label}: {e.filename}")
                    continue
                got[label] = mt
                dt = np.array([mt[t]["timely"] - pt[t]["timely"] for t in tasks])
                df = np.array([mt[t]["fa"] - pt[t]["fa"] for t in tasks])
                bt, bf = dt[draws].sum(1), df[draws].sum(1)
                summ.append(f"| {POLS[pol]} | {RULES[thr]} | {key[6:]} | {label} | {sum(mt[t]['timely'] for t in tasks)} ({dt.sum():+d}) | "
                            f"{np.percentile(bt, 2.5):+.0f} to {np.percentile(bt, 97.5):+.0f} | {(dt > 0).sum()} / {(dt < 0).sum()} / {(dt == 0).sum()} | "
                            f"{sum(mt[t]['fa'] for t in tasks)} ({df.sum():+d}) | {np.percentile(bf, 2.5):+.0f} to {np.percentile(bf, 97.5):+.0f} |")
            for t in tasks:
                cells = [f"{got[m][t]['timely']} / {got[m][t]['fa']}" if m in got else "n/a"
                         for m in ("progress", "gru_phys_ttp s0", "gru_phys_ttp_ens", "or_progress_ttp s0", "or_progress_ens")]
                detail.append(f"| {POLS[pol]} | {RULES[thr]} | {key[6:]} | {t} | {pt[t]['n']} | {pt[t]['ns']} | " + " | ".join(cells) + " |")
lines = ["# Task-level robustness, unseen tasks", "", __doc__.split("\n\n")[0].replace("\n", " "), "", "## Summary", ""] + summ
lines += ["", "## Per task (timely / false alarms)", ""] + detail
if missing:
    lines += ["", "Missing runs (left out): " + "; ".join(missing)]
os.makedirs(args.out, exist_ok=True)
open(os.path.join(args.out, "tasklevel.md"), "w").write("\n".join(lines) + "\n")
print("\n".join(summ[:30]))
