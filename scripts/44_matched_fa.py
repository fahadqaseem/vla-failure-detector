"""Timely alarms at matched false-alarm rates (Fahad, Nov 6, pre-registered in results/plan_nov06.md, item 3). Existing seed 0 scores, no
retraining. For every model the threshold is set on the held-out successes (pooled over the leave-one-task-out folds): the lowest threshold at
which at most a fraction r of successes alarm. So this compares models at the SAME realized false-alarm rate; it is descriptive, not a
deployable rule (a deployed threshold must come from training tasks). Matched rate = progress's realized rate at its own fixed 5% / 2.5%
threshold. Timely = alarm at or before t_pnr, failures with t_pnr > 0. Paired bootstrap over those failures (10000 draws, seed 0, same draws
for both models) with the thresholds held fixed.

python scripts/44_matched_fa.py --out results/matched_fa
"""

import argparse
import json
import os

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

p = argparse.ArgumentParser()
p.add_argument("--runs", nargs="+", default=["OpenVLA-OFT:data/week3_reg", "Pi0.5:data/pi05_reg"], help="policy:root with thr{50,70,80}/unseen")
p.add_argument("--models", nargs="+", default=["gru_phys", "gru_phys_frac", "gru_phys_ttp"])
p.add_argument("--n_boot", type=int, default=10000)
p.add_argument("--out", default="results/matched_fa")
args = p.parse_args()
RATES = np.round(np.arange(0, 0.1001, 0.0025), 4)
RULES = {50: "50% (tau 0.5)", 70: "70% (3 of 4 fail)", 80: "80% (4 of 4 fail)"}
COLORS = {"progress": "#8a8984", "gru_phys": "#2a78d6", "gru_phys_frac": "#eb6834", "gru_phys_ttp": "#1baf7a"}  # gray reference, slots 1-3
MARKERS = {"progress": None, "gru_phys": "o", "gru_phys_frac": "s", "gru_phys_ttp": "^"}


def first_alarm(r, thr):
    s = np.asarray(r["scores"], float)
    above = np.nonzero(s > thr)[0]
    return r["steps"][above[0]] if len(above) else None


def threshold_at(succ_max, rate):
    """Lowest candidate threshold with at most `rate` of the successes above it (ties make some rates unreachable)."""
    cands = np.unique(np.r_[succ_max, np.inf])
    for t in cands:  # ascending: first one that is low enough in false alarms
        if np.mean(succ_max > t) <= rate + 1e-12:
            return t
    return np.inf


def timely_vec(rows, thr):
    return np.array([(lambda a: a is not None and a <= r["t_pnr"])(first_alarm(r, thr)) for r in rows])


lines = ["# Timely alarms at matched false-alarm rates, unseen tasks", "", __doc__.split("\n\n")[0].replace("\n", " "), ""]
table = ["| policy | rule | progress budget | matched false-alarm rate | model | timely | vs progress (95%) |", "|---|---|---|---|---|---|---|"]
curve_rows = ["| policy | rule | model | " + " | ".join(f"{r:.1%}" for r in RATES[::4]) + " |", "|---|---|---|" + "---|" * len(RATES[::4])]
fig, axes = plt.subplots(len(args.runs), 3, figsize=(13, 4.2 * len(args.runs)), sharex=True, squeeze=False)
curves = {}
for i, run in enumerate(args.runs):
    pol, root = run.split(":", 1)
    for j, thr_rule in enumerate(RULES):
        rows = json.load(open(os.path.join(root, f"thr{thr_rule}", "unseen", "all_scores.json")))
        by = {m: [r for r in rows if r["model"] == m] for m in ["progress"] + args.models}
        timed_ids = sorted(r["eid"] for r in by["progress"] if not r["success"] and r["t_pnr"] not in (None, 0))
        n = len(timed_ids)
        draws = np.random.default_rng(0).integers(0, n, (args.n_boot, n))
        tv, succ = {}, {}
        for m, rs in by.items():
            succ[m] = np.array([max(r["scores"]) for r in rs if r["success"]])
            timed = {r["eid"]: r for r in rs if r["eid"] in set(timed_ids)}
            tv[m] = [timed[e] for e in timed_ids]
        # Matched rate: progress's realized false-alarm rate at its own fixed thresholds.
        for key in ("fixed 0.05", "fixed 0.025"):
            fa_p = np.mean([r["alarms"][key] is not None for r in by["progress"] if r["success"]])
            t_p = threshold_at(succ["progress"], fa_p)
            ref = timely_vec(tv["progress"], t_p)
            for m in ["progress"] + args.models:
                t = t_p if m == "progress" else threshold_at(succ[m], fa_p)
                v = timely_vec(tv[m], t)
                real = np.mean(succ[m] > t)
                if m == "progress":
                    vs = "reference"
                else:
                    d = v[draws].sum(1) - ref[draws].sum(1)
                    vs = f"{int(v.sum()) - int(ref.sum()):+d} ({np.percentile(d, 2.5):+.0f} to {np.percentile(d, 97.5):+.0f})"
                table.append(f"| {pol} | {RULES[thr_rule]} | {key[6:]} | {fa_p:.3f} (model realized {real:.3f}) | {m} | {int(v.sum())} of {n} | {vs} |")
        ax = axes[i][j]
        for m in ["progress"] + args.models:
            ys = [timely_vec(tv[m], threshold_at(succ[m], r)).sum() / n for r in RATES]
            curves[(pol, thr_rule, m)] = ys
            ax.plot(RATES * 100, ys, color=COLORS[m], lw=2, ls="--" if m == "progress" else "-", marker=MARKERS[m], ms=4, markevery=4, label=m)
            curve_rows.append(f"| {pol} | {RULES[thr_rule]} | {m} | " + " | ".join(f"{y:.2f}" for y in ys[::4]) + " |")
        ax.set_title(f"{pol}, {RULES[thr_rule]} (n = {n} timed failures)", fontsize=10)
        ax.grid(color="#e6e5e0", lw=0.8)
        ax.set_axisbelow(True)
        for s in ("top", "right"):
            ax.spines[s].set_visible(False)
        if i == len(args.runs) - 1:
            ax.set_xlabel("false alarms on held-out successes (%)")
        if j == 0:
            ax.set_ylabel("timely (fraction of timed failures)")
handles, labels = axes[0][0].get_legend_handles_labels()
fig.legend(handles, labels, loc="upper center", ncol=4, frameon=False)
fig.suptitle("Timely alarms vs matched false-alarm rate, unseen tasks (threshold set on held-out successes, descriptive)", y=0.995, fontsize=11)
fig.tight_layout(rect=(0, 0, 1, 0.95))
os.makedirs(args.out, exist_ok=True)
fig.savefig(os.path.join(args.out, "timely_vs_fa.png"), dpi=150)
lines += ["## At progress's realized false-alarm rate", ""] + table
lines += ["", "## Curve (timely fraction at false-alarm rates 0 to 10%, every 1%); figure timely_vs_fa.png", ""] + curve_rows
open(os.path.join(args.out, "matched_fa.md"), "w").write("\n".join(lines) + "\n")
json.dump({f"{k[0]}|{k[1]}|{k[2]}": v for k, v in curves.items()}, open(os.path.join(args.out, "curves.json"), "w"))
print("\n".join(lines))
