"""Few-shot calibration on the held-out task (Fahad, Nov 7, item 7), existing scores, no retraining, unseen tasks: for each held-out task, k = 5,
10, 20 successes of that task drawn at random (20 draws, seed 0) give the threshold (fixed conformal at the budget; when k is too small for the
budget the conformal rule is infinite, so the max of the k is used instead, which aims at about 1 / (k + 1) false alarms). Scored on the task's
other runs: realized false alarms on its other successes and timely alarms on its failures with t_pnr > 0. Tasks with fewer than k + 1
successes are left out at that k. "training-task threshold" = the usual threshold of the same model.

python scripts/55_fewshot.py --out results/fewshot
"""

import argparse
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from audit_lib import KEYS, POLS, RULES, caught, conformal_threshold, first_alarm, scores, timed  # noqa: E402

p = argparse.ArgumentParser()
p.add_argument("--out", default="results/fewshot")
p.add_argument("--draws", type=int, default=20)
args = p.parse_args()
MODELS = [("progress", "progress", 0), ("gru_phys_ttp s0", "gru_phys_ttp", 0), ("gru_phys_ttp_ens", "gru_phys_ttp_ens", 0)]
lines = ["# Few-shot calibration on the held-out task, unseen tasks", "", __doc__.split("\n\n")[0].replace("\n", " "), "",
         "| policy | rule | budget | model | threshold from | tasks | timely (mean over draws) | false alarms on other successes (mean) |",
         "|---|---|---|---|---|---|---|---|"]
missing = []
for pol in POLS:
    for thr in RULES:
        for label, model, seed in MODELS:
            try:
                rows = scores(pol, thr, model, seed)
            except FileNotFoundError as e:
                missing.append(f"{pol} {thr} {label}: {e.filename}")
                continue
            for key in KEYS:
                a = float(key.split()[1])
                tf, su = [r for r in rows if timed(r)], [r for r in rows if r["success"]]
                lines.append(f"| {POLS[pol]} | {RULES[thr]} | {key[6:]} | {label} | training tasks | {len({r['task'] for r in rows})} | "
                             f"{sum(caught(r, key) for r in tf)} of {len(tf)} | {np.mean([r['alarms'][key] is not None for r in su]):.3f} |")
                for k in (5, 10, 20):
                    rng = np.random.default_rng(0)
                    tim, fas, used, n_t = [], [], 0, 0
                    for t in sorted({r["task"] for r in rows}):
                        st = [r for r in rows if r["task"] == t and r["success"]]
                        ft = [r for r in rows if r["task"] == t and timed(r)]
                        if len(st) < k + 1:
                            continue
                        used += 1
                        n_t += len(ft)
                        mx = np.array([max(r["scores"]) for r in st])
                        tt, ff = [], []
                        for _ in range(args.draws):
                            pick = rng.choice(len(st), k, replace=False)
                            c = conformal_threshold(mx[pick], a)
                            th = mx[pick].max() if np.isinf(c) else c
                            rest = np.setdiff1d(np.arange(len(st)), pick)
                            ff.append(np.mean(mx[rest] > th))
                            tt.append(sum((lambda x: x is not None and x <= r["t_pnr"])(first_alarm(r, th)) for r in ft))
                        tim.append(np.mean(tt))
                        fas.append((np.mean(ff), len(st) - k))
                    fa = sum(f * n for f, n in fas) / max(sum(n for _, n in fas), 1)
                    lines.append(f"| {POLS[pol]} | {RULES[thr]} | {key[6:]} | {label} | k = {k} of the held-out task | {used} | "
                                 f"{sum(tim):.1f} of {n_t} | {fa:.3f} |")
if missing:
    lines += ["", "Missing runs (left out): " + "; ".join(missing)]
os.makedirs(args.out, exist_ok=True)
open(os.path.join(args.out, "fewshot.md"), "w").write("\n".join(lines) + "\n")
print("\n".join(lines[:30]))
