"""Figures for the predictor: t_pnr distribution over the scanned natural failures, and predicted risk vs
true replay risk for 3 example failures.

Example rule (fixed Oct 18 2026, before the results): failures with 0 < t_pnr, one per task, taking the
lowest task ids and, within a task, the lowest init index; first 3.
Predicted risk = held-out score of the logreg and mlp models (each from the fold where its task was held out).

python scripts/07_figures.py --scans "data/full_scans/*.json" --pred results/predictor --out results/predictor
"""

import argparse
import glob
import json
import os
from collections import Counter

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

p = argparse.ArgumentParser()
p.add_argument("--scans", default="data/full_scans/*.json")
p.add_argument("--pred", default="results/predictor")
p.add_argument("--out", default="results/predictor")
p.add_argument("--tau_min_success", type=int, default=3)
args = p.parse_args()


def t_pnr_from_scan(scan):  # same rule as 06_train_predictor.py
    ok = [sum(s) >= args.tau_min_success for s in scan["successes"]]
    if ok[-1]:
        return None
    i = len(ok) - 1
    while i > 0 and not ok[i - 1]:
        i -= 1
    return scan["checkpoints"][i]


scans = [json.load(open(f)) for f in sorted(glob.glob(args.scans))]
fails = [s for s in scans if not s["recorded_success"] and not s["induced"]]
for s in fails:
    s["t_pnr_tau05"] = t_pnr_from_scan(s)

# ---- t_pnr distribution ----
lines = ["# t_pnr over scanned natural failures (full scans, K 4, tau 0.5)", "",
         "| episode | task | t_pnr | t_pnr / 520 |", "|---|---|---|---|"]
for s in fails:
    t = s["t_pnr_tau05"]
    lines.append(f"| {s['episode_id']} | {s['task_id']} | {t} | {'' if t is None else f'{t / 520:.2f}'} |")
vals = sorted(s["t_pnr_tau05"] for s in fails if s["t_pnr_tau05"] is not None)
n_none = sum(s["t_pnr_tau05"] is None for s in fails)
n_zero = sum(v == 0 for v in vals)
pos = [v for v in vals if v > 0]
lines += ["", f"{len(fails)} failures: {len(pos)} with t_pnr > 0, {n_zero} doomed from start (t_pnr 0), "
          f"{n_none} recoverable (no t_pnr)."]
if pos:
    q = lambda f: pos[min(len(pos) - 1, int(f * len(pos)))]  # noqa: E731
    lines.append(f"t_pnr > 0: min {pos[0]}, 25% {q(0.25)}, median {q(0.5)}, 75% {q(0.75)}, max {pos[-1]} (steps).")
lines.append("Per task (t_pnr > 0 / doomed / recoverable): " + ", ".join(
    f"t{t}: {sum(1 for s in fails if s['task_id'] == t and (s['t_pnr_tau05'] or 0) > 0)}/"
    f"{sum(1 for s in fails if s['task_id'] == t and s['t_pnr_tau05'] == 0)}/"
    f"{sum(1 for s in fails if s['task_id'] == t and s['t_pnr_tau05'] is None)}"
    for t in sorted(Counter(s["task_id"] for s in fails))))
text = "\n".join(lines) + "\n"
open(os.path.join(args.out, "t_pnr_distribution.md"), "w").write(text)
print(text)

fig, ax = plt.subplots(figsize=(6, 3.2))
ax.hist(pos, bins=range(0, 528, 32), color="tab:red", alpha=0.8, label="t_pnr > 0")
ax.set_xlabel("t_pnr (policy step, tau 0.5)")
ax.set_ylabel("failures")
ax.set_title(f"t_pnr over {len(fails)} natural failures ({n_zero} doomed at step 0, {n_none} recoverable not shown)",
             fontsize=8)
fig.tight_layout()
fig.savefig(os.path.join(args.out, "t_pnr_hist.png"), dpi=150)

# ---- predicted vs true risk ----
pred = json.load(open(os.path.join(args.pred, "failure_scores.json")))
examples, used_tasks = [], set()
for s in sorted(fails, key=lambda s: (s["task_id"], s["episode_idx"])):
    if (s["t_pnr_tau05"] or 0) > 0 and s["task_id"] not in used_tasks:
        examples.append(s)
        used_tasks.add(s["task_id"])
examples = examples[:3]

fig, axes = plt.subplots(1, len(examples), figsize=(4.2 * len(examples), 3.2), squeeze=False)
for ax, s in zip(axes[0], examples):
    true_risk = [1 - sum(k) / len(k) for k in s["successes"]]
    ax.plot(s["checkpoints"], true_risk, "k.-", label="replay risk (1 - k/4)")
    for model, color in [("logreg", "tab:blue"), ("mlp", "tab:orange")]:
        r = next(r for r in pred if r["model"] == model and r["eid"] == s["episode_id"])
        ax.plot(r["steps"], r["scores"], color=color, label=f"{model} (held out)")
        ax.axhline(r["threshold"], color=color, ls=":", lw=1)
    ax.axvline(s["t_pnr_tau05"], color="tab:red", ls="--", label="t_pnr")
    ax.set_title(f"{s['episode_id']} (task {s['task_id']})", fontsize=9)
    ax.set_xlabel("policy step")
    ax.set_ylim(-0.03, 1.03)
axes[0][0].set_ylabel("risk")
axes[0][0].legend(fontsize=7, loc="upper left")
fig.suptitle("Predicted vs replay risk; dotted = conformal alarm threshold (5% false alarms)", fontsize=9)
fig.tight_layout()
fig.savefig(os.path.join(args.out, "risk_examples.png"), dpi=150)
print("examples:", [s["episode_id"] for s in examples])
