"""Breakdowns (Fahad, Nov 7, item 9), unseen tasks, both policies, all rules (70% main): (1) natural episodes only (timely of natural failures
with t_pnr > 0, false alarms on natural successes); (2) lead-time curve: failures caught at least L = 0, 16, 32, 64 steps before t_pnr;
(3) histogram of alarm steps of the timely catches (70%, both budgets), lead_time.png and alarm_steps.png.

python scripts/57_breakdowns.py --out results/breakdowns
"""

import argparse
import os
import sys

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from audit_lib import KEYS, POLS, RULES, alarms, caught, timed  # noqa: E402

p = argparse.ArgumentParser()
p.add_argument("--out", default="results/breakdowns")
args = p.parse_args()
MODELS = [("progress", "progress", 0), ("gru_phys_ttp s0", "gru_phys_ttp", 0), ("gru_phys_ttp_ens", "gru_phys_ttp_ens", 0),
          ("or_progress_ttp s0", "or_progress_ttp", 0), ("or_progress_ens", "or_progress_ens", 0)]
COLORS = ["#8a8984", "#2a78d6", "#1baf7a", "#eb6834", "#eda100"]
LEADS = [0, 16, 32, 64]
nat = ["| policy | rule | budget | model | natural timely | natural false alarms |", "|---|---|---|---|---|---|"]
lead = ["| policy | rule | budget | model | timed failures | " + " | ".join(f"lead >= {L}" for L in LEADS) + " |", "|---|---|---|---|---|" + "---|" * len(LEADS)]
missing = []
fig, axes = plt.subplots(2, 2, figsize=(11, 7.5), squeeze=False)
fig2, axes2 = plt.subplots(2, 2, figsize=(11, 7.5), squeeze=False)
for i, pol in enumerate(POLS):
    for thr in RULES:
        for j, key in enumerate(KEYS):
            for c, (label, model, seed) in enumerate(MODELS):
                try:
                    rows = alarms(pol, thr, model, seed)
                except FileNotFoundError as e:
                    missing.append(f"{pol} {thr} {label}: {e.filename}")
                    continue
                nt = [r for r in rows if timed(r) and "_p" not in r["eid"]]
                ns = [r for r in rows if r["success"] and "_p" not in r["eid"]]
                nat.append(f"| {POLS[pol]} | {RULES[thr]} | {key[6:]} | {label} | {sum(caught(r, key) for r in nt)} of {len(nt)} | "
                           f"{sum(r['alarms'][key] is not None for r in ns)} of {len(ns)} ({np.mean([r['alarms'][key] is not None for r in ns]):.3f}) |")
                tf = [r for r in rows if timed(r)]
                ld = np.array([r["t_pnr"] - r["alarms"][key] if r["alarms"][key] is not None else -np.inf for r in tf])
                lead.append(f"| {POLS[pol]} | {RULES[thr]} | {key[6:]} | {label} | {len(tf)} | " + " | ".join(str(int((ld >= L).sum())) for L in LEADS) + " |")
                if thr == 70:
                    Ls = np.arange(0, 129, 8)
                    axes[i][j].plot(Ls, [(ld >= L).mean() for L in Ls], color=COLORS[c], lw=2, ls="--" if model == "progress" else "-", label=label)
                    steps = [r["alarms"][key] for r in tf if caught(r, key)]
                    axes2[i][j].hist(steps, bins=np.arange(0, 529, 32), histtype="step", lw=2, color=COLORS[c], label=f"{label} ({len(steps)})")
            for ax, xl, yl in ((axes[i][j], "lead time L (steps before t_pnr)", "fraction of timed failures caught >= L early"),
                               (axes2[i][j], "alarm step of timely catches", "count")):
                ax.set_title(f"{POLS[pol]}, 70% rule, budget {key[6:]}", fontsize=10)
                ax.set_xlabel(xl)
                ax.set_ylabel(yl)
                ax.grid(color="#e6e5e0", lw=0.8)
                ax.set_axisbelow(True)
                for s in ("top", "right"):
                    ax.spines[s].set_visible(False)
                ax.legend(fontsize=7, frameon=False)
os.makedirs(args.out, exist_ok=True)
for f, name, title in ((fig, "lead_time.png", "Lead time before t_pnr, unseen tasks"), (fig2, "alarm_steps.png", "Alarm steps of timely catches, unseen tasks")):
    f.suptitle(title, fontsize=11)
    f.tight_layout(rect=(0, 0, 1, 0.96))
    f.savefig(os.path.join(args.out, name), dpi=150)
lines = ["# Breakdowns, unseen tasks", "", __doc__.split("\n\n")[0].replace("\n", " "), "", "## Natural episodes only", ""] + nat
lines += ["", "## Lead time (failures with t_pnr > 0 caught at least L steps before t_pnr)", ""] + lead
if missing:
    lines += ["", "Missing runs (left out): " + "; ".join(missing)]
open(os.path.join(args.out, "breakdowns.md"), "w").write("\n".join(lines) + "\n")
print("\n".join(lines[:40]))
