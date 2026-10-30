"""Week 3 regression and ablation report (Oct 30): one table per split with every threshold and model, and the regression errors.
Scores come from 06_train_predictor.py runs in ROOT/thr{50,70,80}/{unseen,seen} (28_merge_groups.py already run).
Regression error: gru_phys_frac = mean absolute error of the failure fraction on scanned queries (failures and scanned successes);
gru_phys_ttp = mean absolute error of steps until t_pnr (clipped at 200): all queries of labelled episodes, and failures before t_pnr only.

python scripts/34_reg_report.py --root data/week3_reg --out results/week3/regression
"""

import argparse
import json
import os

import numpy as np

p = argparse.ArgumentParser()
p.add_argument("--root", default="data/week3_reg")
p.add_argument("--out", default="results/week3/regression")
args = p.parse_args()
KEYS = ["fixed 0.05", "fixed 0.025"]


def ours(rows, key):
    """Same definitions as 13_report.py."""
    timed = [r for r in rows if not r["success"] and r["t_pnr"] not in (None, 0)]
    succ = [r for r in rows if r["success"]]
    recov = [r for r in rows if not r["success"] and r["t_pnr"] is None]
    window = [r["alarms"][key] - r["t_pnr"] for r in timed if r["alarms"][key] is not None]
    fa = lambda ss: np.mean([r["alarms"][key] is not None for r in ss]) if ss else float("nan")  # noqa: E731
    return (f"{sum(w <= 0 for w in window)} of {len(timed)} | {fa([r for r in succ if '_p' not in r['eid']]):.3f} / "
            f"{fa([r for r in succ if '_p' in r['eid']]):.3f} | {sum(r['alarms'][key] is not None for r in recov)} of {len(recov)} | "
            + (f"{np.median(window):+.0f}" if window else "none"))


for split in ("unseen", "seen"):
    lines = [f"# Regression and ablation, {split} tasks", "",
             "Natural + perturbed (7 of 10 tasks) + perturbed_v2 (tasks 0, 1, 4, 7), pooled. Timely of failures with t_pnr > 0; false alarms natural / "
             "perturbed successes; unnecessary = alarms on recoverable failures; window = median t_alarm - t_pnr (negative = before t_pnr).", "",
             "| failure threshold | model | " + " | ".join(f"timely {k[6:]} | false alarms {k[6:]} | unnecessary {k[6:]} | window {k[6:]}" for k in KEYS) + " |",
             "|---|---|" + "---|---|---|---|" * len(KEYS)]
    errs = ["", "## Regression error", "", "| failure threshold | model | error | value |", "|---|---|---|---|"]
    for thr in (50, 70, 80):
        rows = json.load(open(os.path.join(args.root, f"thr{thr}", split, "all_scores.json")))
        for m in dict.fromkeys(r["model"] for r in rows):
            mine = [r for r in rows if r["model"] == m]
            lines.append(f"| {thr}% | {m} | " + " | ".join(ours(mine, k) for k in KEYS) + " |")
            if m == "gru_phys_frac":
                s = np.concatenate([r["scores"] for r in mine])
                y = np.concatenate([np.where(np.isnan(r["risk"]) & r["success"], 0.0, r["risk"]) for r in mine])
                scanned = np.concatenate([~np.isnan(np.array(r["risk"], float)) for r in mine])
                ok = ~np.isnan(y)
                errs.append(f"| {thr}% | {m} | MAE failure fraction, scanned queries ({scanned.sum()}) | {np.abs(s - y)[scanned].mean():.3f} |")
                errs.append(f"| {thr}% | {m} | MAE failure fraction, all known queries ({ok.sum()}) | {np.abs(s - y)[ok].mean():.3f} |")
            if m == "gru_phys_ttp":
                s = 200 * (1 - np.concatenate([r["scores"] for r in mine]))
                y = 200 * (1 - np.concatenate([r["ttp"] for r in mine]))
                errs.append(f"| {thr}% | {m} | MAE steps until t_pnr, all queries ({len(y)}) | {np.abs(s - y).mean():.1f} |")
                pre = [(200 * (1 - np.array(r["scores"])), 200 * (1 - np.array(r["ttp"])), np.array(r["labels"])) for r in mine
                       if not r["success"] and r["t_pnr"] not in (None, 0)]
                e = np.concatenate([np.abs(a - b)[lab == 0] for a, b, lab in pre])
                errs.append(f"| {thr}% | {m} | MAE steps until t_pnr, timed failures before t_pnr ({len(e)}) | {e.mean():.1f} |")
    os.makedirs(args.out, exist_ok=True)
    text = "\n".join(lines + errs) + "\n"
    open(os.path.join(args.out, f"table_{split}.md"), "w").write(text)
    print(text)
