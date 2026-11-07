"""Rescue value (Fahad, Nov 7, item 5), unseen tasks: for every alarm on a scanned failure, the retry success fraction at the last scanned
checkpoint at or before the alarm (existing replay scans, K 4, plus the K 12 refinement for OpenVLA-OFT), summed into expected rescues per 100
held-out runs, next to false alarms per 100 runs (alarmed successes). Two versions: retries as scanned (up to 200 steps past the 520-step
limit) and only retries that succeed by step 520. Alarms on unscanned failures (pre-check recoverable) are counted apart, with no value.
A retry here is the same policy restarted from the saved state with action noise 0.05, not a human intervention.

python scripts/54_rescue.py --out results/rescue
"""

import argparse
import glob
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from audit_lib import KEYS, POLS, RULES, alarms, main_models  # noqa: E402

p = argparse.ArgumentParser()
p.add_argument("--out", default="results/rescue")
p.add_argument("--limit", type=int, default=520)
args = p.parse_args()
from audit_scans import load_scans  # noqa: E402


def value(s, step, clock):
    i = max((k for k, c in enumerate(s["c"]) if c <= step), default=None)
    if i is None:
        return None
    ok = [bool(o) and (not clock or e <= args.limit) for o, e in zip(s["ok"][i], s["end"][i])]
    return float(np.mean(ok))


lines = ["# Rescue value of alarms, unseen tasks", "", __doc__.split("\n\n")[0].replace("\n", " "), "",
         "| policy | rule | budget | model | runs | alarms on scanned failures | expected rescues / 100 runs (as scanned) | (by step 520) | "
         "false alarms / 100 runs | alarms on unscanned failures |", "|---|---|---|---|---|---|---|---|---|---|"]
missing = []
for pol in POLS:
    scans = load_scans(pol)
    for thr in RULES:
        for key in KEYS:
            for label, model, seed in main_models():
                try:
                    rows = alarms(pol, thr, model, seed)
                except FileNotFoundError as e:
                    missing.append(f"{pol} {thr} {label}: {e.filename}")
                    continue
                fails = [r for r in rows if not r["success"] and r["alarms"][key] is not None]
                sc = [r for r in fails if r["eid"] in scans]
                v = [value(scans[r["eid"]], r["alarms"][key], False) for r in sc]
                vc = [value(scans[r["eid"]], r["alarms"][key], True) for r in sc]
                n = len(rows)
                fa = sum(r["success"] and r["alarms"][key] is not None for r in rows)
                lines.append(f"| {POLS[pol]} | {RULES[thr]} | {key[6:]} | {label} | {n} | {len(sc)} | {100 * sum(x or 0 for x in v) / n:.2f} | "
                             f"{100 * sum(x or 0 for x in vc) / n:.2f} | {100 * fa / n:.2f} | {len(fails) - len(sc)} |")
if missing:
    lines += ["", "Missing runs (left out): " + "; ".join(missing)]
os.makedirs(args.out, exist_ok=True)
open(os.path.join(args.out, "rescue.md"), "w").write("\n".join(lines) + "\n")
print("\n".join(lines[:30]))
