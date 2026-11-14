"""Plots for the Nov 13 regression (amendment in results/plan_nov13.md): per policy, 4 held-out failed runs and 1 success, the true score
(replay failure fraction at the scanned checkpoints) and every model's predicted score over policy steps on one chart each, seed 0.

Episode choice is a fixed rule, not by result: the failed runs are the kept failures with t_pnr (50% rule) > 0 whose episode id sorts first
in each of 4 different tasks (the 4 tasks with the most kept failures, in task order); the success is the first episode id among the
successes of the first of those tasks. Vertical lines: t_pnr under the 50% rule (solid) and the 70% rule (dotted).

python scripts/62_regression_plots.py --root data/regression_v2 --out results/regression_v2/plots
"""

import argparse
import collections
import glob
import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

p = argparse.ArgumentParser()
p.add_argument("--root", default="data/regression_v2")
p.add_argument("--out", default="results/regression_v2/plots")
p.add_argument("--policies", nargs="+", default=["oft", "pi05"])
p.add_argument("--seed", type=int, default=0)
args = p.parse_args()
MODELS = ["gru_phys_frac", "safe_lin", "safe_mlp", "safe_lstm", "gru_physvla_frac", "const", "progress_iso", "timer_iso"]
NAMES = {"oft": "OpenVLA-OFT", "pi05": "Pi0.5"}
os.makedirs(args.out, exist_ok=True)

for pol in args.policies:
    preds = {}  # model -> eid -> row
    for m in MODELS:
        files = sorted(glob.glob(os.path.join(args.root, pol, m, f"s{args.seed}", "g*.json")))
        if files:
            preds[m] = {r["eid"]: r for f in files for r in json.load(open(f))["rows"]}
    if not preds:
        print(pol, "no runs")
        continue
    rows = next(iter(preds.values()))
    per_task = collections.defaultdict(list)
    for r in rows.values():
        if not r["success"] and r["t50"] not in (None, 0):
            per_task[r["task"]].append(r["eid"])
    tasks = sorted(sorted(per_task, key=lambda t: -len(per_task[t]))[:4])
    picks = [min(per_task[t]) for t in tasks]
    if tasks:
        picks.append(min(e for e, r in rows.items() if r["success"] and r["task"] == tasks[0]))
    for eid in picks:
        r = rows[eid]
        fig, ax = plt.subplots(figsize=(9, 4.5))
        known = [(s, t) for s, t in zip(r["steps"], r["target"]) if t is not None]
        ax.plot([s for s, _ in known], [t for _, t in known], "k.-", lw=2, label="true (replay failure fraction)")
        for m in preds:
            if eid in preds[m]:
                q = preds[m][eid]
                ax.plot(q["steps"], q["pred"], lw=1, ls="--" if m.endswith("_iso") or m == "const" else "-", label=m)
        for key, ls, lab in (("t50", "-", "t_pnr 50%"), ("t70", ":", "t_pnr 70%")):
            if r[key] is not None:
                ax.axvline(r[key], color="gray", ls=ls, label=f"{lab} = {r[key]}")
        ax.set_xlabel("policy step")
        ax.set_ylabel("score")
        ax.set_ylim(-0.02, 1.02)
        ax.set_title(f"{NAMES[pol]} {eid} ({'success' if r['success'] else 'failure'}, held-out task {r['task']}, seed {args.seed})")
        ax.legend(fontsize=7, ncol=2, loc="upper left")
        fig.tight_layout()
        fig.savefig(os.path.join(args.out, f"{pol}_{eid}.png"), dpi=120)
        plt.close(fig)
        print(pol, eid)
