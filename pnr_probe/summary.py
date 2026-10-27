"""Ranking of the feature sets (pnr_probe experiment, Fahad Oct 27 2026), on unseen tasks, once per false-alarm budget
(2.5% and 5%, fixed conformal thresholds):
  1. timely alarms (at or before t_pnr, failures with t_pnr > 0) of the set's best model whose episode-level false
     alarm rate on held-out successes is at or under the budget (models over budget do not count);
  2. ties: median window (t_alarm - t_pnr over alarmed failures) closest to 0.
Models of a set: mlp_phys, gru_phys and their _cusum. progress and Track 1 (t1) are ranked as references.
AUROCs (from 06's summary.md) are a secondary column only. Then the full per-model table, unseen and seen.

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
         "bio": "5a all of 1-4", "bioplus": "5b 1-4 + Track 1", "t1": "Track 1 physical (reference)",
         "progress": "progress (reference)"}
BUDGETS = [("fixed 0.025", 0.025), ("fixed 0.05", 0.05)]


def aurocs(run):
    """model -> (per-step AUROC, time-matched AUROC) from the first table of 06's summary.md."""
    out = {}
    for line in open(os.path.join(run, "summary.md")):
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(c) == 13 and c[0] not in ("model", "---"):
            out[c[0]] = (c[3], c[4])
    return out


def stats(rows, m, k):
    """timely, number timed, FPR on successes, median window (None if no alarm) for model m at key k."""
    succ = [r for r in rows if r["model"] == m and r["success"]]
    timed = [r for r in rows if r["model"] == m and not r["success"] and r["t_pnr"] not in (None, 0)]
    timely = sum(r["alarms"][k] is not None and r["alarms"][k] <= r["t_pnr"] for r in timed)
    window = [r["alarms"][k] - r["t_pnr"] for r in timed if r["alarms"][k] is not None]
    return timely, len(timed), float(np.mean([r["alarms"][k] is not None for r in succ])), \
        float(np.median(window)) if window else None


runs = {}  # (split, set) -> (rows, aurocs)
for s in args.sets:
    for sp in ("unseen", "seen"):
        d = os.path.join(args.results, f"{sp}_{s}")
        if os.path.exists(os.path.join(d, "per_episode.json")):
            runs[(sp, s)] = (json.load(open(os.path.join(d, "per_episode.json"))), aurocs(d))

lines = ["# Bio-inspired precursor features: ranking on unseen tasks", "",
         "All data (natural + perturbed 7 tasks + perturbed_v2 tasks 0, 1, 4, 7, pooled), replay-scan t_pnr labels (refined),",
         "leave-one-task-out. Rank: timely alarms of the set's best model with false alarms on held-out successes at or under",
         "the budget, then median window (t_alarm - t_pnr) closest to 0. Models: mlp_phys, gru_phys, both also _cusum.",
         "AUROC (per-step / time-matched, same model) is secondary. Intervals, paired difference from progress, natural /",
         "perturbed false alarms and unnecessary alarms: unseen_report_fixed_0.025.md and unseen_report_fixed_0.05.md.", ""]
missing = [s for s in args.sets if ("unseen", s) not in runs]
if missing:
    lines += [f"Runs missing (job failed or not finished): {', '.join(missing)}", ""]
unseen = {s: runs[("unseen", s)] for s in args.sets if ("unseen", s) in runs}
for k, budget in BUDGETS:
    cands = []
    for s, (rows, au) in unseen.items():
        models = [m for m in dict.fromkeys(r["model"] for r in rows) if m != "progress"]
        entries = [(m, *stats(rows, m, k)) for m in models]
        ok = [e for e in entries if e[3] <= budget]
        best = max(ok, key=lambda e: (e[1], -abs(e[4]) if e[4] is not None else -np.inf)) if ok else None
        cands.append((s, best, au, min(e[3] for e in entries) if entries else np.nan))
    if unseen:
        rows, au = next(iter(unseen.values()))
        e = ("progress", *stats(rows, "progress", k))
        cands.append(("progress", e if e[3] <= budget else None, au, e[3]))
    cands.sort(key=lambda c: (c[1][1], -abs(c[1][4]) if c[1][4] is not None else -np.inf) if c[1] else (-1, 0), reverse=True)
    lines += [f"## Budget {budget:.1%} false alarms", "",
              "| rank | feature set | best model within budget | timely | false alarms on successes | median window "
              "| AUROC per-step / time-matched |", "|---|---|---|---|---|---|---|"]
    for i, (s, b, au, low) in enumerate(cands, 1):
        if b is None:
            lines.append(f"| {i} | {LABEL.get(s, s)} | none within budget (lowest {low:.4f}) | 0 | | | |")
            continue
        m, t, n, fpr, w = b
        lines.append(f"| {i} | {LABEL.get(s, s)} | {m} | {t} of {n} | {fpr:.3f} | "
                     f"{'none' if w is None else f'{w:+.0f}'} | {' / '.join(au.get(m, ('', '')))} |")
    lines.append("")

lines += ["## Every model (secondary)", "",
          "| split | feature set | model | timely, FPR, window at 2.5% | timely, FPR, window at 5% | AUROC per-step / time-matched |",
          "|---|---|---|---|---|---|"]
fmt = lambda t, n, f, w: f"{t} of {n}, {f:.3f}, {'none' if w is None else f'{w:+.0f}'}"  # noqa: E731
for (sp, s), (rows, au) in runs.items():
    for m in dict.fromkeys(r["model"] for r in rows):
        if m == "progress" and s != next(ss for (spp, ss) in runs if spp == sp):
            continue  # same baseline in every run: once per split
        lines.append(f"| {sp} | {LABEL.get(s, s) if m != 'progress' else 'none'} | {m} | {fmt(*stats(rows, m, 'fixed 0.025'))} | "
                     f"{fmt(*stats(rows, m, 'fixed 0.05'))} | {' / '.join(au.get(m, ('', '')))} |")
open(args.out, "w").write("\n".join(lines) + "\n")
print("\n".join(lines))
