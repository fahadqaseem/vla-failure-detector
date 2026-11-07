"""Rule vs first visible failure (Fahad, Nov 7, item 3): for every failure with t_pnr > 0 under a rule, t_pnr minus the step of the first
07_auto_onset.py event among missed grasp, stuck and drop. Failure type = that first event's type ("none" = no such event). Median and 25 to
75% per rule and type, both policies. Negative = t_pnr comes before the event is visible.

python scripts/52_rule_events.py --out results/rule_events
"""

import argparse
import csv
import json
import os

import numpy as np

p = argparse.ArgumentParser()
p.add_argument("--runs", nargs="+", default=["OpenVLA-OFT:results/week3/patterns/auto_onset.csv:results/week3/relabel/t_pnr_per_rule.json",
                                             "Pi0.5:results/pi05/onset/auto_onset.csv:results/pi05/relabel/t_pnr_per_rule.json"])
p.add_argument("--out", default="results/rule_events")
args = p.parse_args()
TYPES = ("missed_grasp", "stuck", "drop")
RULES = ["50% (labels in use)", "70% (3 of 4 fail)", "80% (4 of 4 fail)"]

lines = ["# t_pnr vs the first visible failure event", "", __doc__.split("\n\n")[0].replace("\n", " "), "",
         "| policy | rule | failure type | failures | median t_pnr - event (steps) | 25 to 75% | t_pnr before the event |", "|---|---|---|---|---|---|---|"]
for run in args.runs:
    pol, onset_csv, rules_json = run.split(":")
    first = {}
    for r in csv.DictReader(open(onset_csv)):
        ev = [(int(x.split()[0]), x.split()[1]) for x in r["events"].split("; ") if x and x.split()[1] in TYPES]
        first[r["episode_id"]] = min(ev) if ev else None
    per = json.load(open(rules_json))
    for rule in RULES:
        by = {}
        for eid, t in per[rule].items():
            if t in (None, 0) or eid not in first:
                continue
            ev = first[eid]
            by.setdefault(ev[1] if ev else "none", []).append(None if ev is None else t - ev[0])
        for typ in list(TYPES) + ["none"]:
            v = [x for x in by.get(typ, []) if x is not None]
            n = len(by.get(typ, []))
            if not n:
                continue
            stat = (f"{np.median(v):+.0f} | {np.percentile(v, 25):+.0f} to {np.percentile(v, 75):+.0f} | {sum(x < 0 for x in v)} of {len(v)}" if v
                    else "n/a | n/a | n/a")
            lines.append(f"| {pol} | {rule} | {typ} | {n} | {stat} |")
os.makedirs(args.out, exist_ok=True)
open(os.path.join(args.out, "rule_events.md"), "w").write("\n".join(lines) + "\n")
print("\n".join(lines))
