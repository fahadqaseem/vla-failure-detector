"""One compact table over the feature sets (pnr_probe experiment): for each run, AUROCs from 06's summary.md and
timely / false positive rate on successes at 5% and 2.5% (fixed conformal) from per_episode.json.
"Most signal" = the feature set whose best learned model (mlp_phys or gru_phys, no CUSUM, since CUSUM only
re-scores) has the highest time-matched AUROC on unseen tasks (threshold free, and counting time helps little).

python pnr_probe/summary.py --results pnr_probe/results --sets surprise csd ttc micro bio bioplus t1 --out pnr_probe/results/summary.md
"""

import argparse
import json
import os

import numpy as np

p = argparse.ArgumentParser()
p.add_argument("--results", required=True)
p.add_argument("--sets", nargs="+", required=True)
p.add_argument("--out", required=True)
args = p.parse_args()

LABEL = {"surprise": "1 surprise", "csd": "2 critical slowing down", "ttc": "3 time-to-contact", "micro": "4 micro-events",
         "bio": "5a all of 1-4", "bioplus": "5b 1-4 + Track 1", "t1": "Track 1 physical (baseline)"}


def aurocs(run):
    """model -> (per-step AUROC, time-matched AUROC) from the first table of 06's summary.md."""
    out = {}
    for line in open(os.path.join(run, "summary.md")):
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(c) == 13 and c[0] not in ("model", "---"):
            out[c[0]] = (c[3], c[4])
    return out


def counts(rows, m, k):
    succ = [r for r in rows if r["model"] == m and r["success"]]
    timed = [r for r in rows if r["model"] == m and not r["success"] and r["t_pnr"] not in (None, 0)]
    timely = sum(r["alarms"][k] is not None and r["alarms"][k] <= r["t_pnr"] for r in timed)
    return f"{timely} of {len(timed)}, FPR {np.mean([r['alarms'][k] is not None for r in succ]):.3f}"


lines = ["# Bio-inspired precursor features: summary", "",
         "All data (natural + perturbed 7 tasks + perturbed_v2 tasks 0, 1, 4, 7, pooled), replay-scan t_pnr labels (refined).",
         "Timely = alarm at or before t_pnr of failures with t_pnr > 0; FPR = episode-level false alarms on held-out successes;",
         "thresholds fixed conformal. Intervals, paired difference from progress, natural / perturbed FPR, unnecessary alarms",
         "and median window: unseen_report_fixed_0.05.md and _0.025.md. tm-AUROC = time-matched per-step AUROC.", "",
         "| feature set | model | unseen tm-AUROC | unseen per-step AUROC | unseen timely, FPR at 5% | unseen timely, FPR at 2.5% "
         "| seen tm-AUROC | seen timely, FPR at 5% |", "|---|---|---|---|---|---|---|---|"]
best, shown = {}, False
for s in args.sets:
    runs = {sp: os.path.join(args.results, f"{sp}_{s}") for sp in ("unseen", "seen")}
    if not os.path.exists(os.path.join(runs["unseen"], "per_episode.json")):
        lines.append(f"| {LABEL.get(s, s)} | run missing | | | | | | |")
        continue
    data = {sp: (json.load(open(os.path.join(r, "per_episode.json"))), aurocs(r))
            for sp, r in runs.items() if os.path.exists(os.path.join(r, "per_episode.json"))}
    rows, au = data["unseen"]
    for m in dict.fromkeys(r["model"] for r in rows):
        if m == "progress" and shown:
            continue  # same baseline in every run: shown once
        shown = shown or m == "progress"
        seen = data.get("seen")
        lines.append(f"| {LABEL.get(s, s) if m != 'progress' else 'none (baseline)'} | {m} | {au.get(m, ('', ''))[1]} | "
                     f"{au.get(m, ('', ''))[0]} | {counts(rows, m, 'fixed 0.05')} | {counts(rows, m, 'fixed 0.025')} | "
                     + (f"{seen[1].get(m, ('', ''))[1]} | {counts(seen[0], m, 'fixed 0.05')} |" if seen else " | |"))
        if m in ("mlp_phys", "gru_phys") and s != "t1":
            best[s] = max(best.get(s, -1), float(au[m][1]))
if best:
    top = max(best, key=best.get)
    lines += ["", f"Most signal (best unseen time-matched AUROC of mlp_phys / gru_phys, bio sets only): {LABEL[top]} "
              f"({best[top]:.3f}). All: " + ", ".join(f"{s} {v:.3f}" for s, v in sorted(best.items(), key=lambda x: -x[1]))]
open(args.out, "w").write("\n".join(lines) + "\n")
print("\n".join(lines))
