"""Report for 60_regression.py (Nov 13 plan, results/plan_nov13.md). Pooled over the 10 held-out tasks.

  report.md          seed 0: MSE and MAE on (i) scanned checkpoints of failed runs, (ii) successes, (iii) all known points; Spearman on
                     failed runs (pooled over points, and median per episode with a non-constant target); binomial noise floor.
  per_task.md        seed 0: MSE (i) and (ii) per held-out task.
  backup_alarms.md   seed 0: % of timed failures (t_pnr > 0) caught at or before t_pnr at a 2.5% false-alarm threshold, 50% and 70% rules.
  best2.txt          the two learned models with the lowest mean over both policies of (MSE (i) + MSE (ii)) / 2 at seed 0.
  seeds.md           (with --seed_models) mean and std over seeds 0 to 4 of the main metrics.

Noise floor per point with K retries and observed failure fraction f: MSE f(1 - f) / (K - 1) (unbiased for the binomial variance of f);
MAE E|X/K - f| with X ~ Binomial(K, f) (plug-in, approximate). Points with an assumed target 0 (K 0) have floor 0.

python scripts/61_regression_report.py --root data/regression_v2 --out results/regression_v2
"""

import argparse
import glob
import json
import os

import numpy as np
from scipy.stats import binom, spearmanr

p = argparse.ArgumentParser()
p.add_argument("--root", default="data/regression_v2")
p.add_argument("--out", default="results/regression_v2")
p.add_argument("--policies", nargs="+", default=["oft", "pi05"])
p.add_argument("--seed_models", nargs="*", default=None, help="models with seeds 0 to 4: write seeds.md")
p.add_argument("--alpha", type=float, default=0.025)
args = p.parse_args()
LEARNED = ["gru_phys_frac", "safe_lin", "safe_mlp", "safe_lstm", "gru_physvla_frac"]
MODELS = LEARNED + ["const", "progress_iso", "timer_iso"]
NAMES = {"oft": "OpenVLA-OFT", "pi05": "Pi0.5"}


def load(policy, model, seed):
    files = sorted(glob.glob(os.path.join(args.root, policy, model, f"s{seed}", "g*.json")))
    if len(files) != 10:
        return None
    runs = [json.load(open(f)) for f in files]
    return dict(rows=[r for run in runs for r in run["rows"]], calib={run["held_out"]: [c[1] for c in run["calib"]] for run in runs},
                counts=runs[0]["counts"])


def points(rows):
    out = {k: [] for k in ("pred", "target", "K", "success", "eid", "task")}
    for r in rows:
        for pr, t, k in zip(r["pred"], r["target"], r["K"]):
            if t is not None:
                for key, v in (("pred", pr), ("target", t), ("K", k), ("success", r["success"]), ("eid", r["eid"]), ("task", r["task"])):
                    out[key].append(v)
    return {k: np.array(v) for k, v in out.items()}


def floors(target, K):
    mse, mae = np.zeros(len(target)), np.zeros(len(target))
    for i, (f, k) in enumerate(zip(target, K)):
        if k > 1:
            mse[i] = f * (1 - f) / (k - 1)
            x = np.arange(k + 1)
            mae[i] = (binom.pmf(x, k, f) * np.abs(x / k - f)).sum()
    return mse.mean(), mae.mean()


def metrics(rows):
    P = points(rows)
    out = {}
    for part, m in (("fail", ~P["success"]), ("succ", P["success"]), ("all", np.ones(len(P["pred"]), bool))):
        e = P["pred"][m] - P["target"][m]
        out[part] = dict(mse=float((e ** 2).mean()), mae=float(np.abs(e).mean()), n=int(m.sum()), floor=floors(P["target"][m], P["K"][m]))
    f = ~P["success"]
    out["rho"] = float(spearmanr(P["pred"][f], P["target"][f])[0]) if np.ptp(P["pred"][f]) > 0 else float("nan")
    per = []
    for eid in np.unique(P["eid"][f]):
        m = f & (P["eid"] == eid)
        if np.ptp(P["target"][m]) > 0 and np.ptp(P["pred"][m]) > 0:
            per.append(spearmanr(P["pred"][m], P["target"][m])[0])
    out["rho_ep"], out["n_rho_ep"] = (float(np.median(per)) if per else float("nan")), len(per)
    out["per_task"] = {}
    for t in range(10):
        row = {}
        for part, m in (("fail", f), ("succ", P["success"])):
            m = m & (P["task"] == t)
            row[part] = (float(((P["pred"][m] - P["target"][m]) ** 2).mean()), int(m.sum())) if m.any() else (None, 0)
        out["per_task"][t] = row
    return out


def conformal_threshold(run_maxes, alpha):  # same as 06_train_predictor.py
    n = len(run_maxes)
    k = int(np.ceil((n + 1) * (1 - alpha)))
    return np.inf if k > n else float(np.sort(run_maxes)[k - 1])


def backup(run):
    thr = {g: conformal_threshold(np.array(c), args.alpha) for g, c in run["calib"].items()}
    alarm = {}
    for r in run["rows"]:
        above = [s for s, v in zip(r["steps"], r["pred"]) if v > thr[r["task"]]]
        alarm[r["eid"]] = above[0] if above else None
    succ = [r for r in run["rows"] if r["success"]]
    out = dict(fa=sum(alarm[r["eid"]] is not None for r in succ), n_succ=len(succ))
    for rule in ("t50", "t70"):
        timed = [r for r in run["rows"] if not r["success"] and r[rule] not in (None, 0)]
        out[rule] = (sum(alarm[r["eid"]] is not None and alarm[r["eid"]] <= r[rule] for r in timed), len(timed))
    return out


fmt = lambda x: "n/a" if x is None or np.isnan(x) else f"{x:.4f}"  # noqa: E731
os.makedirs(args.out, exist_ok=True)
res, runs = {}, {}
for pol in args.policies:
    for m in MODELS:
        run = load(pol, m, 0)
        if run:
            runs[pol, m], res[pol, m] = run, metrics(run["rows"])

head = ["# Pure regression of the point of no return score, seed 0 (plan: results/plan_nov13.md)", "",
        "Target = replay failure fraction at each query; MSE only, every episode weighted equally; leave one task out (10 held-out tasks, "
        "pooled over points). (i) scanned checkpoints of failed runs, (ii) successes (target 0 unless scanned), (iii) all known points. "
        "Spearman on failed runs: pooled over points / median per episode (episodes with a non-constant target). Floor = binomial noise of "
        "the retries (K 4, or 16 where refined); it is the error a perfect predictor of the true failure probability would still have.", ""]
lines = list(head)
for pol in args.policies:
    any_run = next((runs[pol, m] for m in MODELS if (pol, m) in runs), None)
    if any_run is None:
        lines += [f"## {NAMES[pol]}: no complete runs", ""]
        continue
    c = any_run["counts"]
    lines += [f"## {NAMES[pol]}", "",
              f"Kept: {c['kept_episodes']} episodes ({c['kept_failures']} failures, {c['kept_successes']} successes), {c['known_points']} known "
              f"points. Excluded failures: {c['precheck_recoverable']} recoverable by pre-check, {c['scan_recoverable']} scanned and recoverable "
              f"(50% rule), {c['unscanned_failures']} unscanned (no target). Hidden states present in every kept episode.", "",
              "| model | MSE (i) fail | MAE (i) | MSE (ii) succ | MAE (ii) | MSE (iii) all | MAE (iii) | Spearman fail pooled | per episode (n) |",
              "|---|---|---|---|---|---|---|---|---|"]
    for m in MODELS:
        if (pol, m) not in res:
            lines.append(f"| {m} | missing |  |  |  |  |  |  |  |")
            continue
        r = res[pol, m]
        lines.append(f"| {m} | {fmt(r['fail']['mse'])} | {fmt(r['fail']['mae'])} | {fmt(r['succ']['mse'])} | {fmt(r['succ']['mae'])} | "
                     f"{fmt(r['all']['mse'])} | {fmt(r['all']['mae'])} | {fmt(r['rho'])} | {fmt(r['rho_ep'])} ({r['n_rho_ep']}) |")
    r = res[pol, next(m for m in MODELS if (pol, m) in res)]
    lines += [f"| noise floor | {fmt(r['fail']['floor'][0])} | {fmt(r['fail']['floor'][1])} | {fmt(r['succ']['floor'][0])} | "
              f"{fmt(r['succ']['floor'][1])} | {fmt(r['all']['floor'][0])} | {fmt(r['all']['floor'][1])} |  |  |",
              "", f"Points: (i) {r['fail']['n']}, (ii) {r['succ']['n']}, (iii) {r['all']['n']}. timer_iso is a check (policy step mapped by "
              "isotonic regression), not a candidate.", ""]

score = {m: np.mean([(res[pol, m]["fail"]["mse"] + res[pol, m]["succ"]["mse"]) / 2 for pol in args.policies])
         for m in LEARNED if all((pol, m) in res for pol in args.policies)}
best = sorted(score, key=score.get)[:2]
lines += ["## Best two learned models (pre-registered rule)", "",
          "Lowest mean over both policies of (MSE (i) + MSE (ii)) / 2 at seed 0:", ""]
lines += [f"- {m}: {score[m]:.4f}" + (" (picked)" if m in best else "") for m in sorted(score, key=score.get)]
open(os.path.join(args.out, "report.md"), "w").write("\n".join(lines) + "\n")
open(os.path.join(args.out, "best2.txt"), "w").write(" ".join(best) + "\n")

lines = ["# Per held-out task, seed 0: MSE (i) failed runs (points) / MSE (ii) successes (points)", ""]
for pol in args.policies:
    ms = [m for m in MODELS if (pol, m) in res]
    lines += [f"## {NAMES[pol]}", "", "| task | " + " | ".join(ms) + " |", "|---|" + "---|" * len(ms)]
    for t in range(10):
        cells = []
        for m in ms:
            (a, na), (b, nb) = res[pol, m]["per_task"][t]["fail"], res[pol, m]["per_task"][t]["succ"]
            cells.append(f"{fmt(a)} ({na}) / {fmt(b)} ({nb})")
        lines.append(f"| {t} | " + " | ".join(cells) + " |")
    lines.append("")
open(os.path.join(args.out, "per_task.md"), "w").write("\n".join(lines) + "\n")

lines = ["# Backup only: alarms from the regression scores, seed 0", "",
         f"Threshold per held-out task = conformal quantile (alpha {args.alpha}) of the per-run max score of the training-task successes, "
         "cross-fitted (each training task scored by a model trained on the other 8). Alarm = first query above it. Timely = alarm at or "
         "before t_pnr, of the kept failures with t_pnr > 0 under that rule. False alarms = held-out successes with any alarm.", "",
         "| policy | model | timely 50% rule | timely 70% rule | false alarms on successes |", "|---|---|---|---|---|"]
for pol in args.policies:
    for m in MODELS:
        if (pol, m) in runs:
            b = backup(runs[pol, m])
            pct = lambda x: f"{x[0]} of {x[1]} ({100 * x[0] / x[1]:.0f}%)" if x[1] else "n/a"  # noqa: E731
            lines.append(f"| {NAMES[pol]} | {m} | {pct(b['t50'])} | {pct(b['t70'])} | {b['fa']} of {b['n_succ']} ({b['fa'] / b['n_succ']:.3f}) |")
open(os.path.join(args.out, "backup_alarms.md"), "w").write("\n".join(lines) + "\n")

if args.seed_models:
    keys = [("MSE (i)", lambda r: r["fail"]["mse"]), ("MSE (ii)", lambda r: r["succ"]["mse"]), ("MSE (iii)", lambda r: r["all"]["mse"]),
            ("MAE (i)", lambda r: r["fail"]["mae"]), ("Spearman fail", lambda r: r["rho"])]
    lines = ["# Seeds 0 to 4 for the best two learned models (mean +- std over seeds; n = seeds found)", "",
             "| policy | model | " + " | ".join(k for k, _ in keys) + " | seeds |", "|---|---|" + "---|" * (len(keys) + 1)]
    for pol in args.policies:
        for m in args.seed_models:
            rs = [metrics(r["rows"]) for r in (load(pol, m, s) for s in range(5)) if r]
            cells = [f"{np.mean([f(r) for r in rs]):.4f} +- {np.std([f(r) for r in rs]):.4f}" for _, f in keys] if rs else ["n/a"] * len(keys)
            lines.append(f"| {NAMES[pol]} | {m} | " + " | ".join(cells) + f" | {len(rs)} |")
    open(os.path.join(args.out, "seeds.md"), "w").write("\n".join(lines) + "\n")
print(open(os.path.join(args.out, "best2.txt")).read())
