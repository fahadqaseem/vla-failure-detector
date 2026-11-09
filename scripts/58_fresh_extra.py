"""Fresh Pi0.5 test extras (Fahad, Nov 9): on data/pi05_fresh/thr{T}/{split}/merged/per_episode.json (models trained on the old episodes, scored
on the new perturbed seeds 2 to 4 only): (1) task bootstrap as results/tasklevel (per-task timely and false alarms vs progress, 10000 draws over
the held-out tasks, seed 0, tasks better / worse / equal); (2) rescue value as results/rescue (retry success fraction at the last scanned
checkpoint at or before each alarm on a scanned failure, per 100 runs; as scanned and by step 520), next to false alarms per 100 runs.

python scripts/58_fresh_extra.py --root data/pi05_fresh --out results/pi05/fresh/extra.md
"""

import argparse
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from audit_lib import KEYS, RULES, caught, timed  # noqa: E402
from audit_scans import load_scans  # noqa: E402

p = argparse.ArgumentParser()
p.add_argument("--root", default="data/pi05_fresh")
p.add_argument("--out", default="results/pi05/fresh/extra.md")
args = p.parse_args()
scans = load_scans("pi05")


def value(s, step, clock):
    i = max((k for k, c in enumerate(s["c"]) if c <= step), default=None)
    if i is None:
        return 0.0
    return float(np.mean([bool(o) and (not clock or e <= 520) for o, e in zip(s["ok"][i], s["end"][i])]))


boot = ["| split | rule | budget | model | timely (vs progress) | bootstrap over tasks (95%) | tasks better / worse / equal | false alarms (vs progress) |",
        "|---|---|---|---|---|---|---|---|"]
resc = ["| split | rule | budget | model | runs | alarms on scanned failures | expected rescues / 100 runs (as scanned) | (by step 520) | false alarms / 100 runs |",
        "|---|---|---|---|---|---|---|---|---|"]
for split in ("unseen", "seen"):
    for thr in RULES:
        rows = json.load(open(os.path.join(args.root, f"thr{thr}", split, "merged", "per_episode.json")))
        models = list(dict.fromkeys(r["model"] for r in rows))
        tasks = sorted({r["task"] for r in rows})
        draws = np.random.default_rng(0).integers(0, len(tasks), (10000, len(tasks)))
        for key in KEYS:
            tt = {m: np.array([sum(caught(r, key) for r in rows if r["model"] == m and r["task"] == t and timed(r)) for t in tasks]) for m in models}
            fa = {m: np.array([sum(r["alarms"][key] is not None for r in rows if r["model"] == m and r["task"] == t and r["success"]) for t in tasks]) for m in models}
            for m in models:
                mine = [r for r in rows if r["model"] == m]
                n = len(mine)
                al = [r for r in mine if not r["success"] and r["alarms"][key] is not None and r["eid"] in scans]
                v = sum(value(scans[r["eid"]], r["alarms"][key], False) for r in al)
                vc = sum(value(scans[r["eid"]], r["alarms"][key], True) for r in al)
                nfa = sum(r["success"] and r["alarms"][key] is not None for r in mine)
                resc.append(f"| {split} | {RULES[thr]} | {key[6:]} | {m} | {n} | {len(al)} | {100 * v / n:.2f} | {100 * vc / n:.2f} | {100 * nfa / n:.2f} |")
                if m == "progress":
                    continue
                d = tt[m] - tt["progress"]
                b = d[draws].sum(1)
                boot.append(f"| {split} | {RULES[thr]} | {key[6:]} | {m} | {tt[m].sum()} ({d.sum():+d}) | {np.percentile(b, 2.5):+.0f} to "
                            f"{np.percentile(b, 97.5):+.0f} | {(d > 0).sum()} / {(d < 0).sum()} / {(d == 0).sum()} | {fa[m].sum()} ({fa[m].sum() - fa['progress'].sum():+d}) |")
lines = ["# Fresh Pi0.5 test: task bootstrap and rescue value", "", __doc__.split("\n\n")[0].replace("\n", " "), "", "## Task bootstrap", ""] + boot
lines += ["", "## Rescue value", ""] + resc
os.makedirs(os.path.dirname(args.out), exist_ok=True)
open(args.out, "w").write("\n".join(lines) + "\n")
print("\n".join(lines[:20]))
