"""Did the OR ensemble stay within its budget? (Oct 31). Actual false alarms per held-out task for or_25, or_50, or_75, and, for any setting whose actual
rate is within 5%, timely alarms against progress at its 5% threshold (paired bootstrap over timed failures, 10000 draws, seed 0). That comparison
is chosen after seeing the rates, so it is a lead to test, not a result.

python scripts/39_or_budget.py --dir results/week3/complementarity
"""

import argparse
import json
import os

import numpy as np

p = argparse.ArgumentParser()
p.add_argument("--dir", default="results/week3/complementarity")
args = p.parse_args()
rows = json.load(open(os.path.join(args.dir, "per_episode.json")))
by = {}
for r in rows:
    by.setdefault(r["model"], {})[r["eid"]] = r
timed = sorted((e, r["t_pnr"]) for e, r in by["progress"].items() if not r["success"] and r["t_pnr"] not in (None, 0))
hit = lambda m, k: np.array([by[m][e]["alarms"][k] is not None and by[m][e]["alarms"][k] <= t for e, t in timed])  # noqa: E731
draws = np.random.default_rng(0).integers(0, len(timed), (10000, len(timed)))
ref = hit("progress", "fixed 0.05")
lines = ["# OR ensemble: actual false alarms", "", __doc__.split("\n\n")[0].replace("\n", " "), "",
         "| model | target | actual false alarms | natural / perturbed | worst tasks (rate) | timely | vs progress at 5% (17 timely) |", "|---|---|---|---|---|---|---|"]
for m in ("or_25", "or_50", "or_75"):
    for k in ("fixed 0.05", "fixed 0.025"):
        succ = [r for r in by[m].values() if r["success"]]
        fa = lambda ss: np.mean([r["alarms"][k] is not None for r in ss])  # noqa: E731
        task = {t: fa([r for r in succ if r["task"] == t]) for t in range(10)}
        worst = sorted(task, key=task.get, reverse=True)[:3]
        h = hit(m, k)
        vs = "over 5%, not compared"
        if fa(succ) <= 0.05:
            d = h[draws].sum(1) - ref[draws].sum(1)
            vs = f"{int(h.sum() - ref.sum()):+d} ({np.percentile(d, 2.5):+.0f} to {np.percentile(d, 97.5):+.0f})"
        lines.append(f"| {m} | {k[6:]} | {fa(succ):.3f} | {fa([r for r in succ if '_p' not in r['eid']]):.3f} / {fa([r for r in succ if '_p' in r['eid']]):.3f} | "
                     + ", ".join(f"t{t} {task[t]:.2f}" for t in worst) + f" | {int(h.sum())} of {len(timed)} | {vs} |")
open(os.path.join(args.dir, "budget_check.md"), "w").write("\n".join(lines) + "\n")
print("\n".join(lines))
