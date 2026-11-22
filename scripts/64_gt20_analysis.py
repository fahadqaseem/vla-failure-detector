"""Pilot analysis of the 20-replay ground truth (results/plan_nov22_gt20.md, Step 3). CPU, reads JSON only.

Per pilot run (data/gt20_pilot/<eid>/c*.json, checkpoints every 16 steps, 20 replays each):
  - truth = failure fraction with K 20, and with K 8 and K 4 as random subsets of the 20 (--draws draws each, fixed rng), one figure;
  - mean absolute change vs K 20 (mean over checkpoints and draws), also for the original K 4 truth (the 4 seed-0 scan replays).
Slide redraw (Nov 20) for --slide_run: K 20 truth with the seed 0 predictions of data/regression_v2 (models, colours, line styles and legend
as 62_regression_plots.py; old K 4 truth in light grey).
MSE of each model (seed 0) vs the K 4 truth and vs the K 20 truth at the pilot checkpoints, per run and pooled.

python scripts/64_gt20_analysis.py --pilot data/gt20_pilot --out results/gt20
"""

import argparse
import glob
import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from scipy.stats import beta  # noqa: E402

p = argparse.ArgumentParser()
p.add_argument("--pilot", default="data/gt20_pilot")
p.add_argument("--reg", default="data/regression_v2/oft")
p.add_argument("--out", default="results/gt20")
p.add_argument("--draws", type=int, default=10)
p.add_argument("--K", type=int, default=20)
p.add_argument("--slide_run", default="t00_e06_p0_s1")
args = p.parse_args()
MODELS = ["gru_phys_frac", "safe_lin", "safe_mlp", "safe_lstm", "gru_physvla_frac", "const", "progress_iso", "timer_iso"]  # as 62
os.makedirs(os.path.join(args.out, "plots"), exist_ok=True)
rng = np.random.default_rng(22)


def t_pnr50(cps, succ):
    """50% rule (Jeffreys lower 0.25 quantile >= 0.5 = recoverable); first checkpoint from which all later ones are not recoverable."""
    ok = [beta.ppf(0.25, sum(s) + 0.5, len(s) - sum(s) + 0.5) >= 0.5 for s in succ]
    if ok[-1]:
        return None
    i = len(ok) - 1
    while i > 0 and not ok[i - 1]:
        i -= 1
    return cps[i]


preds = {}  # model -> eid -> row
for m in MODELS:
    for f in glob.glob(os.path.join(args.reg, m, "s0", "g*.json")):
        for r in json.load(open(f))["rows"]:
            preds.setdefault(m, {})[r["eid"]] = r

runs = {}
for d in sorted(glob.glob(os.path.join(args.pilot, "*"))):
    cs = [json.load(open(f)) for f in sorted(glob.glob(os.path.join(d, "c*.json")))]
    cs = [c for c in cs if len(c["replays"]) >= args.K]
    if cs:
        runs[os.path.basename(d)] = cs

lines = ["# 20-replay ground truth, pilot (plan: results/plan_nov22_gt20.md, Step 3)", "",
         f"OpenVLA-OFT, checkpoints every 16 steps, K {args.K} (seed 0 scan replays and seed 1 refinement replays reused where present, "
         f"new replays seed 20), noise 0.05, extra_steps 200. K 8 and K 4 = random subsets of the 20 ({args.draws} draws each, rng 22). "
         "Original K 4 = the 4 seed-0 replays of the existing scan. Failure fraction = 1 - successes / K.", "",
         "## Change of the truth vs K 20 (mean absolute difference of the failure fraction over checkpoints and draws)", "",
         "| run | checkpoints | K 4 subsets | K 8 subsets | original K 4 (seed 0) | t_pnr 50%: K 4 every 8 (scan) | K 20 every 16 |",
         "|---|---|---|---|---|---|---|"]
pool = {"k4": [], "k8": [], "orig": []}
truth = {}
for eid, cs in runs.items():
    cps = [c["checkpoint"] for c in cs]
    S = np.array([[r["success"] for r in c["replays"][: args.K]] for c in cs])  # (checkpoints, K)
    seed0 = np.array([[r["success"] for r in c["replays"] if r["seed"] == 0 and r["source"] == "reused"] for c in cs])
    f20 = 1 - S.mean(1)
    sub = {k: np.array([1 - S[:, rng.choice(args.K, k, replace=False)].mean(1) for _ in range(args.draws)]) for k in (4, 8)}
    f_orig = 1 - seed0.mean(1)
    truth[eid] = dict(cps=cps, f20=f20, f4=f_orig, S=S)
    ch = {k: np.abs(sub[k] - f20).mean() for k in (4, 8)}
    ch_o = np.abs(f_orig - f20).mean()
    pool["k4"] += list(np.abs(sub[4] - f20).ravel())
    pool["k8"] += list(np.abs(sub[8] - f20).ravel())
    pool["orig"] += list(np.abs(f_orig - f20))
    any_row = next((preds[m][eid] for m in preds if eid in preds[m]), None)
    t_old = any_row["t50"] if any_row else None
    lines.append(f"| {eid} | {len(cps)} | {ch[4]:.3f} | {ch[8]:.3f} | {ch_o:.3f} | {t_old} | {t_pnr50(cps, S.tolist())} |")
    fig, ax = plt.subplots(figsize=(9, 4.5))
    for k, col in ((4, "tab:orange"), (8, "tab:blue")):
        for j in range(args.draws):
            ax.plot(cps, sub[k][j], color=col, lw=0.7, alpha=0.35, label=f"K {k} (random subsets of the 20, {args.draws} draws)" if j == 0 else None)
    ax.plot(cps, f_orig, color="gray", ls="--", lw=1.2, label="K 4 original (seed 0 scan replays)")
    ax.plot(cps, f20, "k.-", lw=2, label="K 20")
    ax.set_xlabel("policy step")
    ax.set_ylabel("replay failure fraction")
    ax.set_ylim(-0.02, 1.02)
    ax.set_title(f"OpenVLA-OFT {eid}: truth with K 4, 8, 20 (checkpoints every 16 steps)")
    ax.legend(fontsize=7, loc="upper left")
    fig.tight_layout()
    fig.savefig(os.path.join(args.out, "plots", f"truth_K_{eid}.png"), dpi=120)
    plt.close(fig)
if pool["k4"]:
    lines.append(f"| all | {sum(len(t['cps']) for t in truth.values())} | {np.mean(pool['k4']):.3f} | {np.mean(pool['k8']):.3f} | "
                 f"{np.mean(pool['orig']):.3f} |  |  |")
missing = [e for e in ("t00_e06_p0_s1", "t01_e07_p0_s1", "t04_e00_p0_s2") if e not in runs]
lines += ["", f"Runs with checkpoints still missing or not started: {missing or 'none'}; checkpoints done per run: "
          + ", ".join(f"{e} {len(c)}" for e, c in runs.items()) + ".", ""]

# ---- model MSE vs K 4 and K 20 truth at the pilot checkpoints ----
lines += ["## Seed 0 model predictions (data/regression_v2, unseen task) vs the K 4 and K 20 truth, pilot checkpoints", "",
          "MSE over the checkpoints every 16 steps of the pilot runs (pooled; per run in brackets: " + ", ".join(runs) + "). "
          "K 4 = original seed 0 scan replays. Noise floor = mean f(1 - f) / (K - 1) of that truth.", "",
          "| model | MSE vs K 4 truth | MSE vs K 20 truth |", "|---|---|---|"]
for m in MODELS:
    if m not in preds:
        continue
    e4, e20, per = [], [], []
    for eid, t in truth.items():
        if eid not in preds[m]:
            continue
        r = preds[m][eid]
        pr = dict(zip(r["steps"], r["pred"]))
        x = np.array([pr[c] for c in t["cps"]])
        a, b = (x - t["f4"]) ** 2, (x - t["f20"]) ** 2
        e4 += list(a)
        e20 += list(b)
        per.append((a.mean(), b.mean()))
    if e4:
        lines.append(f"| {m} | {np.mean(e4):.4f} ({', '.join(f'{a:.3f}' for a, _ in per)}) | "
                     f"{np.mean(e20):.4f} ({', '.join(f'{b:.3f}' for _, b in per)}) |")
fl4 = np.mean([f * (1 - f) / 3 for t in truth.values() for f in t["f4"]]) if truth else float("nan")
fl20 = np.mean([f * (1 - f) / (args.K - 1) for t in truth.values() for f in t["f20"]]) if truth else float("nan")
lines += [f"| noise floor | {fl4:.4f} | {fl20:.4f} |", ""]

# ---- slide redraw ----
eid = args.slide_run
if eid in truth and any(eid in preds[m] for m in preds):
    t = truth[eid]
    r0 = next(preds[m][eid] for m in MODELS if m in preds and eid in preds[m])
    fig, ax = plt.subplots(figsize=(9, 4.5))
    known = [(s, v) for s, v in zip(r0["steps"], r0["target"]) if v is not None]
    ax.plot([s for s, _ in known], [v for _, v in known], color="lightgray", lw=1, marker=".", ms=3, label="old truth K 4 (every 8)")
    ax.plot(t["cps"], t["f20"], "k.-", lw=2, label="true (replay failure fraction, K 20)")
    for i, m in enumerate(m for m in MODELS if m in preds):
        if eid in preds[m]:
            q = preds[m][eid]
            ax.plot(q["steps"], q["pred"], lw=1, ls="--" if m.endswith("_iso") or m == "const" else "-", color=f"C{i}", label=m)
    t20 = t_pnr50(t["cps"], t["S"].tolist())
    for v, ls, lab in ((r0["t50"], "-", "t_pnr 50% (K 4)"), (r0["t70"], ":", "t_pnr 70% (K 4)"), (t20, "-.", "t_pnr 50% (K 20)")):
        if v is not None:
            ax.axvline(v, color="gray" if "K 4" in lab else "black", ls=ls, label=f"{lab} = {v}")
    ax.set_xlabel("policy step")
    ax.set_ylabel("score")
    ax.set_ylim(-0.02, 1.02)
    ax.set_title(f"OpenVLA-OFT {eid} (failure, held-out task {r0['task']}, seed 0), truth with K 20")
    ax.legend(fontsize=7, ncol=2, loc="upper left")
    fig.tight_layout()
    fig.savefig(os.path.join(args.out, "plots", f"slide_{eid}_K20.png"), dpi=120)
    plt.close(fig)
    lines.append(f"Slide redraw: plots/slide_{eid}_K20.png. Per run truth curves: plots/truth_K_<run>.png.")
open(os.path.join(args.out, "pilot.md"), "w").write("\n".join(lines) + "\n")
print("\n".join(lines))
