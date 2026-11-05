"""Paired bootstrap intervals vs progress for the regression models (Fahad, Oct 31), unseen tasks. Same method as 13_report.py: read from its
report rows (10000 draws over timed failures, same draws for both models), so nothing is recomputed.

python scripts/40_intervals.py --dir results/week3/regression --out results/week3/regression/intervals.md
"""

import argparse
import json
import os

import numpy as np

p = argparse.ArgumentParser()
p.add_argument("--dir", default="results/week3/regression")
p.add_argument("--out", default="results/week3/regression/intervals.md")
p.add_argument("--scores", default="data/week3_reg")
p.add_argument("--thrs", nargs="+", type=int, default=[70, 80], help="failure thresholds in %%")
args = p.parse_args()
lines = ["# gru_phys_frac and gru_phys_ttp vs progress, unseen tasks", "", __doc__.split("\n\n")[0].replace("\n", " ") + " An interval that holds 0 is no evidence of a difference.", "",
         "| failure threshold | target | model | timely (95%) | vs progress (95%) | false alarms on successes | unnecessary alarms |", "|---|---|---|---|---|---|---|"]
for thr in args.thrs:
    for key in ("0.05", "0.025"):
        for line in open(os.path.join(args.dir, f"thr{thr}_unseen_report_fixed_{key}.md")):
            c = [x.strip() for x in line.split("|")]
            if len(c) == 11 and c[2] in ("progress", "gru_phys_frac", "gru_phys_ttp"):
                lines.append(f"| {thr}% | {float(key) * 100:g}% | {c[2]} | {c[3]} | {c[5] or 'reference'} | {c[7]} | {c[8]} |")
lines += ["", "## Unnecessary alarms and false alarms vs progress", "",
          "Same bootstrap (10000 draws, seed 0, same draws for both models), over recoverable failures and over successes of the held-out tasks. "
          "Difference = model minus progress in counts of alarmed runs; negative = fewer alarms than progress. Scores from " + args.scores + ".", "",
          "| failure threshold | target | model | unnecessary alarms | vs progress (95%) | false alarms | vs progress (95%) |", "|---|---|---|---|---|---|---|"]
for thr in args.thrs:
    rows = json.load(open(os.path.join(args.scores, f"thr{thr}", "unseen", "per_episode.json")))
    for key in ("fixed 0.05", "fixed 0.025"):
        al = {(r["model"], r["eid"]): r["alarms"][key] is not None for r in rows}
        cols = []
        recov = sorted({r["eid"] for r in rows if not r["success"] and r["t_pnr"] is None})
        succ = sorted({r["eid"] for r in rows if r["success"]})
        for m in ("gru_phys_frac", "gru_phys_ttp"):
            cols = []
            for ids in (recov, succ):
                a = np.array([al[(m, e)] for e in ids])
                b = np.array([al[("progress", e)] for e in ids])
                draws = np.random.default_rng(0).integers(0, len(ids), (10000, len(ids)))
                d = a[draws].sum(1) - b[draws].sum(1)
                cols += [f"{a.sum()} vs {b.sum()} of {len(ids)}", f"{int(a.sum()) - int(b.sum()):+d} ({np.percentile(d, 2.5):+.0f} to {np.percentile(d, 97.5):+.0f})"]
            lines.append(f"| {thr}% | {float(key[6:]) * 100:g}% | {m} | " + " | ".join(cols) + " |")
open(args.out, "w").write("\n".join(lines) + "\n")
print("\n".join(lines))
