"""Paired bootstrap intervals vs progress for the regression models (Fahad, Oct 31), unseen tasks. Same method as 13_report.py: read from its
report rows (10000 draws over timed failures, same draws for both models), so nothing is recomputed.

python scripts/40_intervals.py --dir results/week3/regression --out results/week3/regression/intervals.md
"""

import argparse
import os

p = argparse.ArgumentParser()
p.add_argument("--dir", default="results/week3/regression")
p.add_argument("--out", default="results/week3/regression/intervals.md")
args = p.parse_args()
lines = ["# gru_phys_frac and gru_phys_ttp vs progress, unseen tasks", "", __doc__.split("\n\n")[0].replace("\n", " ") + " An interval that holds 0 is no evidence of a difference.", "",
         "| failure threshold | target | model | timely (95%) | vs progress (95%) | false alarms on successes | unnecessary alarms |", "|---|---|---|---|---|---|---|"]
for thr in (70, 80):
    for key in ("0.05", "0.025"):
        for line in open(os.path.join(args.dir, f"thr{thr}_unseen_report_fixed_{key}.md")):
            c = [x.strip() for x in line.split("|")]
            if len(c) == 11 and c[2] in ("progress", "gru_phys_frac", "gru_phys_ttp"):
                lines.append(f"| {thr}% | {float(key) * 100:g}% | {c[2]} | {c[3]} | {c[5] or 'reference'} | {c[7]} | {c[8]} |")
open(args.out, "w").write("\n".join(lines) + "\n")
print("\n".join(lines))
