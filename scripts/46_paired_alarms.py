"""Paired bootstrap vs progress for unnecessary alarms (recoverable failures) and false alarms (successes), as results/week3/regression/intervals.md
(10000 draws, seed 0, same draws for both models). Reads DIR/per_episode.json of any run (Nov 6 plan: combo, realistic).

python scripts/46_paired_alarms.py --pred data/combo/oft/thr50/merged --out results/combo/oft_thr50_alarms.md
"""

import argparse
import json
import os

import numpy as np

p = argparse.ArgumentParser()
p.add_argument("--pred", nargs="+", required=True)
p.add_argument("--keys", nargs="+", default=["fixed 0.05", "fixed 0.025"])
p.add_argument("--reference", default="progress")
p.add_argument("--out", required=True)
args = p.parse_args()
lines = ["# Unnecessary and false alarms vs " + args.reference, "", __doc__.split("\n\n")[0].replace("\n", " ") +
         " Difference = model minus reference in alarmed runs; negative = fewer alarms.", "",
         "| run | budget | model | unnecessary alarms | vs reference (95%) | false alarms | vs reference (95%) |", "|---|---|---|---|---|---|---|"]
for pred in args.pred:
    rows = json.load(open(os.path.join(pred, "per_episode.json")))
    models = [m for m in dict.fromkeys(r["model"] for r in rows) if m != args.reference]
    recov = sorted({r["eid"] for r in rows if not r["success"] and r["t_pnr"] is None})
    succ = sorted({r["eid"] for r in rows if r["success"]})
    for key in args.keys:
        al = {(r["model"], r["eid"]): r["alarms"][key] is not None for r in rows}
        for m in models:
            cols = []
            for ids in (recov, succ):
                a = np.array([al[(m, e)] for e in ids])
                b = np.array([al[(args.reference, e)] for e in ids])
                draws = np.random.default_rng(0).integers(0, len(ids), (10000, len(ids)))  # same draws for both (paired)
                d = a[draws].sum(1) - b[draws].sum(1)
                cols += [f"{a.sum()} vs {b.sum()} of {len(ids)}", f"{int(a.sum()) - int(b.sum()):+d} ({np.percentile(d, 2.5):+.0f} to {np.percentile(d, 97.5):+.0f})"]
            lines.append(f"| {pred} | {key[6:]} | {m} | " + " | ".join(cols) + " |")
os.makedirs(os.path.dirname(args.out), exist_ok=True)
open(args.out, "w").write("\n".join(lines) + "\n")
print("\n".join(lines))
