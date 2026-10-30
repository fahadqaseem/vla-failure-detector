"""Report for FailureSpot's methods on our data (30_fs_run.py), Fahad Oct 30: per_episode.json for 13_report.py and one table with
our metrics and FailureSpot's (timestamp and trajectory AUROC, its binary_auroc). LOTO is pooled over the 10 held-out tasks; own =
mean over seeds 0 to 2, unseen tasks only (its seen evaluation set gives the thresholds). gru_phys comes from
results/week3/failurespot/gru_phys/unseen.

python scripts/31_fs_report.py --root results/week3/failurespot
"""

import argparse
import glob
import json
import os
import sys

import numpy as np

sys.path.insert(0, "third_party/failurespot/src")
from failurespot.metrics import binary_auroc  # noqa: E402

p = argparse.ArgumentParser()
p.add_argument("--root", default="results/week3/failurespot")
p.add_argument("--progress", default="results/week2/T1all_unseen_conv/per_episode.json")
args = p.parse_args()
METHODS = [f"{m}_{a}" for m in ("failurespot", "safe", "supervised_random", "actprobe") for a in ("mlp", "lstm")] + ["logpzo"]
KEYS = ["fixed 0.05", "fixed 0.025"]


def ours(rows, key):
    """Our report's columns (same definitions as 13_report.py)."""
    timed = [r for r in rows if not r["success"] and r["t_pnr"] not in (None, 0)]
    succ = [r for r in rows if r["success"]]
    recov = [r for r in rows if not r["success"] and r["t_pnr"] is None]
    window = [r["alarms"][key] - r["t_pnr"] for r in timed if r["alarms"][key] is not None]
    fa = lambda ss: float(np.mean([r["alarms"][key] is not None for r in ss])) if ss else float("nan")  # noqa: E731
    return dict(timely=sum(w <= 0 for w in window), timed=len(timed), fa_nat=fa([r for r in succ if "_p" not in r["eid"]]),
                fa_pert=fa([r for r in succ if "_p" in r["eid"]]),
                unnecessary=sum(r["alarms"][key] is not None for r in recov), recov=len(recov),
                window=float(np.median(window)) if window else float("nan"))


def aurocs(scores, labels, lengths, failed):
    ends = np.cumsum(lengths)[:-1]
    return binary_auroc(labels, scores), binary_auroc(failed, [s.max() for s in np.split(scores, ends)])


def cells(o):
    return (f"{o['timely']:.3g} of {o['timed']:.3g} | {o['fa_nat']:.3f} / {o['fa_pert']:.3f} | "
            f"{o['unnecessary']:.3g} of {o['recov']:.3g} | {o['window']:+.0f}")


lines = ["# FailureSpot methods vs gru_phys on our data", "",
         "Timely of failures with t_pnr > 0; false alarms natural / perturbed successes; unnecessary = alarms on recoverable failures; "
         "window = median t_alarm - t_pnr over alarmed failures (negative = before t_pnr). AUROC: FailureSpot's metrics, labels 1 from "
         "t_pnr on. Natural and perturbed pooled (7 of 10 tasks perturbed, perturbed_v2 tasks 0, 1, 4, 7). own = its split, seeds 0 to 2, "
         "unseen tasks, mean; loto = leave one task out, pooled.", "",
         "| split | model | timestamp AUROC | trajectory AUROC | " + " | ".join(
             f"timely {k[6:]} | false alarms {k[6:]} | unnecessary {k[6:]} | window {k[6:]}" for k in KEYS) + " |",
         "|---|---|---|---|" + "---|---|---|---|" * len(KEYS)]
loto_rows = [r for r in json.load(open(args.progress)) if r["model"] == "progress"]
for m in METHODS:
    fs = [os.path.join(args.root, "loto", f"g{g}", m) for g in range(10)]
    have = [f for f in fs if os.path.exists(f + ".json")]
    if len(have) < 10:
        print(f"loto {m}: only {len(have)} of 10 groups", flush=True)
        if not have:
            continue
    rows = [r for f in have for r in json.load(open(f + ".json"))["rows"]["held_out"]]
    loto_rows += rows
    z = [np.load(f + ".npz") for f in have]
    auc = aurocs(np.concatenate([x["scores"] for x in z]), np.concatenate([x["labels"] for x in z]),
                 np.concatenate([x["lengths"] for x in z]), [not r["success"] for r in rows])
    note = "" if len(have) == 10 else f" ({len(have)} of 10 tasks)"
    lines.append(f"| loto | {m}{note} | {auc[0]:.3f} | {auc[1]:.3f} | " + " | ".join(cells(ours(rows, k)) for k in KEYS) + " |")
os.makedirs(os.path.join(args.root, "loto"), exist_ok=True)
json.dump(loto_rows, open(os.path.join(args.root, "loto", "per_episode.json"), "w"))
gp = os.path.join(args.root, "gru_phys", "unseen", "all_scores.json")
if os.path.exists(gp):
    rows = [r for r in json.load(open(gp)) if r["model"] == "gru_phys"]
    auc = aurocs(np.concatenate([r["scores"] for r in rows]), np.concatenate([r["labels"] for r in rows]),
                 [len(r["scores"]) for r in rows], [not r["success"] for r in rows])
    lines.append(f"| loto | gru_phys (ours) | {auc[0]:.3f} | {auc[1]:.3f} | " + " | ".join(cells(ours(rows, k)) for k in KEYS) + " |")
for m in METHODS:
    per = []
    for s in range(3):
        f = os.path.join(args.root, "own", f"g{s}", m + ".json")
        if os.path.exists(f):
            per.append(json.load(open(f)))
    if not per:
        continue
    means = [{c: float(np.mean([ours(x["rows"]["unseen"], k)[c] for x in per])) for c in ("timely", "timed", "fa_nat", "fa_pert", "unnecessary", "recov", "window")}
             for k in KEYS]
    a = [np.mean([x["metrics"]["unseen"][c] for x in per]) for c in ("timestamp_auroc", "trajectory_auroc")]
    note = "" if len(per) == 3 else f" ({len(per)} of 3 seeds)"
    lines.append(f"| own | {m}{note} | {a[0]:.3f} | {a[1]:.3f} | " + " | ".join(cells(o) for o in means) + " |")
for s in range(3):
    rows = [r for f in sorted(glob.glob(os.path.join(args.root, "own", f"g{s}", "*.json"))) if not f.endswith("per_episode.json")
            for r in json.load(open(f))["rows"]["unseen"]]
    json.dump(rows, open(os.path.join(args.root, "own", f"g{s}", "per_episode.json"), "w"))
open(os.path.join(args.root, "table.md"), "w").write("\n".join(lines) + "\n")
print("\n".join(lines))
