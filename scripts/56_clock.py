"""Clock-aware labels (Fahad, Nov 7, item 8): t_pnr recomputed from the existing scans counting a retry as a success only if it succeeds by step
520 (the episode's own limit), with the same three rules as 32_relabel.py (Jeffreys tau 0.5, raw failure fraction >= 0.7, >= 0.8). Existing
alarms are rescored without retraining: OUT/{pol}_thr{T}/per_episode.json for 13_report.py, and a count of how labels move (recoverable ->
timed, timed -> doomed, ...). Unscanned failures (pre-check recoverable) keep their label.

python scripts/56_clock.py --out data/clock
"""

import argparse
import json
import os
import sys
from collections import Counter

import numpy as np
from scipy.stats import beta

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from audit_lib import DROP, POLS, RULES, alarms, main_models  # noqa: E402
from audit_scans import load_scans  # noqa: E402

p = argparse.ArgumentParser()
p.add_argument("--out", default="data/clock")
p.add_argument("--limit", type=int, default=520)
args = p.parse_args()
jeff = lambda x: beta.ppf(0.25, sum(x) + 0.5, len(x) - sum(x) + 0.5) >= 0.5  # noqa: E731
RULE = {50: jeff, 70: lambda x: 1 - sum(x) / len(x) < 0.7, 80: lambda x: 1 - sum(x) / len(x) < 0.8}


def t_pnr(s, rule):
    ok = [rule([bool(o) and e <= args.limit for o, e in zip(oks, ends)]) for oks, ends in zip(s["ok"], s["end"])]
    if ok[-1]:
        return None
    i = len(ok) - 1
    while i > 0 and not ok[i - 1]:
        i -= 1
    return s["c"][i]


kind = lambda t: "recoverable" if t is None else ("doomed" if t == 0 else "timed")  # noqa: E731
lines = ["# Clock-aware labels: label changes", "", __doc__.split("\n\n")[0].replace("\n", " "), "",
         "| policy | rule | failures | old -> new label (count) |", "|---|---|---|---|"]
for pol in POLS:
    scans = load_scans(pol)
    for thr in RULES:
        new = {e: t_pnr(s, RULE[thr]) for e, s in scans.items()}
        rows_out, moves = [], Counter()
        for label, model, seed in main_models():
            try:
                rows = alarms(pol, thr, model, seed)
            except FileNotFoundError:
                continue
            for r in rows:
                r2 = {k: v for k, v in r.items() if k not in DROP}
                if not r["success"] and r["eid"] in new:
                    r2["t_pnr"] = new[r["eid"]]
                    r2["doomed"] = r2["t_pnr"] == 0
                    if model == "progress":
                        moves[f"{kind(r['t_pnr'])} -> {kind(r2['t_pnr'])}"] += 1
                rows_out.append(dict(r2, model=label.replace(" ", "_")))
        d = os.path.join(args.out, f"{pol}_thr{thr}")
        os.makedirs(d, exist_ok=True)
        json.dump(rows_out, open(os.path.join(d, "per_episode.json"), "w"), indent=0)
        lines.append(f"| {POLS[pol]} | {RULES[thr]} | {sum(moves.values())} | " + "; ".join(f"{k} ({v})" for k, v in sorted(moves.items())) + " |")
os.makedirs("results/clock", exist_ok=True)
open("results/clock/label_changes.md", "w").write("\n".join(lines) + "\n")
print("\n".join(lines))
