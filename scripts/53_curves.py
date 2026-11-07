"""One curve per policy, every method (Fahad, Nov 7, item 4), 70% rule, unseen tasks: timely alarms (at or before t_pnr, failures with t_pnr >
0) against the realized false-alarm rate on held-out successes, 0 to 10%. Thresholds are swept on the held-out successes, pooled over folds, so
this is descriptive, not a deployable rule. Methods: progress, SAFE-style and Hide-and-Seek-style (06, data/base70), FailureSpot (mlp, lstm)
and its action probe (Pi0.5) from results/*/failurespot/loto, the gru_phys_ttp seed ensemble, and progress OR the ensemble (common level q for
both parts on the held-out successes, best q at each rate). FailureSpot scores were trained on 50% labels; they are scored here against the 70%
t_pnr. Evaluation set: the held-out episodes of our 70% runs that each method scored.

python scripts/53_curves.py --out results/curves
"""

import argparse
import json
import os
import sys

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from audit_lib import POLS, first_alarm, scores, threshold_at, timed  # noqa: E402

p = argparse.ArgumentParser()
p.add_argument("--out", default="results/curves")
args = p.parse_args()
RATES = np.round(np.arange(0, 0.1001, 0.0025), 4)
FS = {"oft": ("results/week3/failurespot/loto", ["failurespot_mlp", "failurespot_lstm"]),
      "pi05": ("results/pi05/failurespot/loto", ["failurespot_mlp", "failurespot_lstm", "actprobe_mlp", "actprobe_lstm"])}
COLORS = {"progress": "#8a8984", "safe": "#6250d6", "hideseek": "#e87ba4", "failurespot_mlp": "#eda100", "failurespot_lstm": "#c98500",
          "actprobe_mlp": "#e34948", "actprobe_lstm": "#b03030", "gru_phys_ttp_ens": "#1baf7a", "or_progress_ens": "#2a78d6"}


def sweep(rows):
    succ = np.array([max(r["scores"]) for r in rows if r["success"]])
    tf = [r for r in rows if timed(r)]
    out = []
    for rate in RATES:
        th = threshold_at(succ, rate)
        out.append((float(np.mean(succ > th)), sum((lambda a: a is not None and a <= r["t_pnr"])(first_alarm(r, th)) for r in tf)))
    return out, len(tf)


def sweep_or(pr, en):
    ids = [r["eid"] for r in pr]
    pm = {r["eid"]: r for r in pr}
    em = {r["eid"]: r for r in en}
    succ = [e for e in ids if pm[e]["success"]]
    ps, es = np.array([max(pm[e]["scores"]) for e in succ]), np.array([max(em[e]["scores"]) for e in succ])
    tf = [e for e in ids if timed(pm[e])]
    pts = []
    for q in np.linspace(0, 0.2, 161):
        tp, tg = threshold_at(ps, q), threshold_at(es, q)
        fa = float(np.mean((ps > tp) | (es > tg)))
        hit = 0
        for e in tf:
            a = [x for x in (first_alarm(pm[e], tp), first_alarm(em[e], tg)) if x is not None]
            hit += bool(a) and min(a) <= pm[e]["t_pnr"]
        pts.append((fa, hit))
    return [max([(f, h) for f, h in pts if f <= rate + 1e-12], key=lambda x: x[1], default=(0.0, 0)) for rate in RATES], len(tf)


lines = ["# Timely vs realized false alarms, every method, 70% rule, unseen tasks", "", __doc__.split("\n\n")[0].replace("\n", " "), "",
         "| policy | method | timed failures | " + " | ".join(f"timely at <= {r:.1%} (realized)" for r in (0.01, 0.025, 0.05, 0.10)) + " |",
         "|---|---|---|---|---|---|---|"]
fig, axes = plt.subplots(1, 2, figsize=(13, 5), squeeze=False)
curves = {}
for i, pol in enumerate(POLS):
    ref = scores(pol, 70, "progress")
    by_eid = {r["eid"]: r for r in ref}
    methods = {"progress": ref}
    for m in ("safe", "hideseek"):
        f = f"data/base70/{pol}/{m}/all_scores.json"
        if os.path.exists(f):
            methods[m] = [r for r in json.load(open(f)) if r["model"] == m]
    root, fsm = FS[pol]
    for m in fsm:
        rows = []
        for g in range(10):
            f = os.path.join(root, f"g{g}", m + ".npz")
            if not os.path.exists(f):
                continue
            z = np.load(f)
            ends = np.cumsum(z["lengths"])[:-1]
            for e, s in zip(z["eids"], np.split(z["scores"], ends)):
                e = str(e)
                if e in by_eid and len(s) == len(by_eid[e]["steps"]):
                    rows.append(dict(by_eid[e], scores=s.tolist()))
        if rows:
            methods[m] = rows
    try:
        methods["gru_phys_ttp_ens"] = scores(pol, 70, "gru_phys_ttp_ens")
    except FileNotFoundError:
        pass
    for m, rows in methods.items():
        res, n = sweep(rows)
        curves[(pol, m)] = (res, n)
    if "gru_phys_ttp_ens" in methods:
        curves[(pol, "or_progress_ens")] = sweep_or(ref, methods["gru_phys_ttp_ens"])
    ax = axes[0][i]
    for m in [k for (pp, k) in curves if pp == pol]:
        res, n = curves[(pol, m)]
        ax.plot(RATES * 100, [h / n for _, h in res], lw=2, color=COLORS.get(m, "#333333"), ls="--" if m == "progress" else "-", label=m)
        pick = [res[int(np.argmin(np.abs(RATES - r)))] for r in (0.01, 0.025, 0.05, 0.10)]
        lines.append(f"| {POLS[pol]} | {m} | {n} | " + " | ".join(f"{h} ({f:.3f})" for f, h in pick) + " |")
    ax.set_title(f"{POLS[pol]}, 70% rule", fontsize=10)
    ax.set_xlabel("false alarms on held-out successes (%)")
    ax.set_ylabel("timely (fraction of timed failures)")
    ax.set_ylim(bottom=0)
    ax.grid(color="#e6e5e0", lw=0.8)
    ax.set_axisbelow(True)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.legend(fontsize=7, frameon=False, loc="upper left")
fig.suptitle("Timely vs realized false alarms, unseen tasks (thresholds swept on held-out successes, descriptive)", fontsize=11)
fig.tight_layout(rect=(0, 0, 1, 0.95))
os.makedirs(args.out, exist_ok=True)
fig.savefig(os.path.join(args.out, "curves.png"), dpi=150)
open(os.path.join(args.out, "curves.md"), "w").write("\n".join(lines) + "\n")
print("\n".join(lines))
