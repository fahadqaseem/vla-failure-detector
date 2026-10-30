"""Every model in the papers' metrics (Fahad, Oct 30), from per_episode.json of 06_train_predictor.py. No training.

per-step AUROC       label 1 at and after t_pnr, whole run (our label, not a paper's), all labelled episodes
time-matched AUROC   same, label-1 steps vs success steps in the same 64-step bin (a timer gets about 0.5)
trajectory AUROC     max score of the run, failure vs success (trajectory labels, as SAFE and Hide-and-Seek train)
bACC, wACC, TWA      Hide-and-Seek's metrics: failures = positives, successes = negatives, TP = any alarm, time-varying
                     threshold; mean over alpha 0.15, 0.20, 0.25 where the run has them, else alpha 0.20 only (marked *)
Failures here are all labelled failures (timed, doomed from start, recoverable), as trajectory labels count them.

python scripts/27_paper_metrics.py --pred results/week3/baselines/unseen results/week2/T1all_unseen_conv --out table.md
"""

import argparse
import json
import os

import numpy as np
from sklearn.metrics import roc_auc_score

p = argparse.ArgumentParser()
p.add_argument("--pred", nargs="+", required=True)
p.add_argument("--bin", type=int, default=64)
p.add_argument("--out", required=True)
args = p.parse_args()


def clean(s):
    """Gated models: -inf where the gate is closed, ranked below every other step."""
    s = np.asarray(s, float)
    f = np.isfinite(s)
    return np.where(f, s, s[f].min() - 1 if f.any() else 0.0)


def time_matched(y, s, steps, succ):
    total, pairs = 0.0, 0
    for b in np.unique(steps // args.bin):
        here = steps // args.bin == b
        pos, neg = s[here & (y == 1)], s[here & succ]
        if len(pos) and len(neg):
            total += roc_auc_score(np.r_[np.ones(len(pos)), np.zeros(len(neg))], np.r_[pos, neg]) * len(pos) * len(neg)
            pairs += len(pos) * len(neg)
    return total / pairs if pairs else float("nan")


def accuracies(rows, key, length):
    fails = [r for r in rows if not r["success"]]
    succ = [r for r in rows if r["success"]]
    tpr = np.mean([r["alarms"][key] is not None for r in fails])
    tnr = np.mean([r["alarms"][key] is None for r in succ])
    beta = len(succ) / len(rows)
    early = [1 - r["alarms"][key] / length[r["eid"]] for r in fails if r["alarms"][key] is not None]
    return (tpr + tnr) / 2, beta * tnr + (1 - beta) * tpr, (sum(early) / len(fails) + tnr) / 2


def summary_aurocs(pred):
    """Older runs saved no success scores, so their step AUROCs come from the first table of summary.md."""
    out = {}
    for line in open(os.path.join(pred, "summary.md")):
        c = [x.strip() for x in line.split("|")]
        if len(c) > 5 and c[1] not in out and c[1] not in ("model", "---"):
            try:
                out[c[1]] = float(c[4]), float(c[5])
            except ValueError:
                pass
    return out


lines = ["# Models in the papers' metrics", "",
         "See scripts/27_paper_metrics.py for the definitions. * = only alpha 0.20 is available for that run. "
         "n/a = the run did not save success scores.", "",
         "| run | model | per-step AUROC | time-matched AUROC | trajectory AUROC | bACC | wACC | TWA |", "|---|---|---|---|---|---|---|---|"]
seen = set()
for pred in args.pred:
    full = os.path.join(pred, "all_scores.json")
    rows = json.load(open(full if os.path.exists(full) else os.path.join(pred, "per_episode.json")))
    length = {(r["model"], r["eid"]): r["steps"][-1] + 8 for r in json.load(open(os.path.join(pred, "failure_scores.json")))}
    old = None if os.path.exists(full) else summary_aurocs(pred)
    split = "unseen" if "unseen" in pred else "seen"
    for m in dict.fromkeys(r["model"] for r in rows):
        if (split, m) in seen:  # progress is in every run of a split
            continue
        seen.add((split, m))
        mine = [r for r in rows if r["model"] == m]
        if old is None:
            y = np.concatenate([r["labels"] for r in mine])
            s = clean(np.concatenate([r["scores"] for r in mine]))
            steps = np.concatenate([r["steps"] for r in mine])
            succ = np.concatenate([np.full(len(r["steps"]), r["success"]) for r in mine])
            top = np.array([np.max(clean(r["scores"])) for r in mine])
            auc, tm = roc_auc_score(y, s), time_matched(y, s, steps, succ)
            traj = f"{roc_auc_score([not r['success'] for r in mine], top):.3f}"
        else:
            auc, tm = old[m]
            traj = "n/a"
        keys = [k for k in ("time-varying 0.15", "time-varying 0.20", "time-varying 0.25") if k in mine[0]["alarms"]]
        mark = "" if len(keys) == 3 else "*"
        ln = {r["eid"]: length[(m, r["eid"])] for r in mine if not r["success"]}
        acc = np.mean([accuracies(mine, k, ln) for k in keys], axis=0)
        lines.append(f"| {pred} | {m} | {auc:.3f} | {tm:.3f} | {traj} | {acc[0]:.3f}{mark} | {acc[1]:.3f}{mark} | {acc[2]:.3f}{mark} |")
open(args.out, "w").write("\n".join(lines) + "\n")
print("\n".join(lines))
