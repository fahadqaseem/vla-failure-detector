"""Patterns at t_pnr (Prof. Zhu meeting, Oct 30). Timed failures are split by 07_auto_onset.py events: type = first event at or after t_pnr
(none = silent). A second table uses the first event of the whole run. Signals from data/physical over the goal objects used by the task:
gripper distance = smallest distance, tilt = largest tilt, contact = any contact (articulation slot included), median and 25 to 75% per
step relative to t_pnr, -200 to +100, 8-step queries. First contact = first query with contact: compared with t_pnr at 50, 70, 80%; contact
is sampled every 8 steps, so a touch between queries is not seen. Writes clip_ids.txt for 36_pnr_clips.py (fixed rule: round robin over the
types, lowest id first, 10 ids).

python scripts/35_patterns.py --onsets results/week3/patterns/auto_onset.csv --out results/week3/patterns
"""

import argparse
import csv
import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

p = argparse.ArgumentParser()
p.add_argument("--onsets", default="results/week3/patterns/auto_onset.csv")
p.add_argument("--rules", default="results/week3/relabel/t_pnr_per_rule.json")
p.add_argument("--phys", default="data/physical")
p.add_argument("--out", default="results/week3/patterns")
args = p.parse_args()

rules = json.load(open(args.rules))
T = {"50%": rules["50% (labels in use)"], "70%": rules["70% (3 of 4 fail)"], "80%": rules["80% (4 of 4 fail)"]}
rows = {r["episode_id"]: r for r in csv.DictReader(open(args.onsets))}
TYPES = ["missed_grasp", "drop", "stuck", "wrong_object", "none"]


def signals(eid):
    d = np.load(os.path.join(args.phys, eid + ".npz"))
    x, names = d["x"], d["names"].tolist()
    col = lambda n: x[:, names.index(n)]  # noqa: E731
    used = [i for i in (1, 2) if col(f"obj{i}_used").max() > 0]
    dist = [col(f"obj{i}_dist") for i in used] + ([col("art_dist")] if col("art_used").max() > 0 else [])
    touch = [col(f"obj{i}_contact") for i in used] + ([col("art_contact")] if col("art_used").max() > 0 else [])
    tilt = np.max([col(f"obj{i}_tilt") for i in used], 0) if used else np.full(len(x), np.nan)
    return d["query_steps"], np.min(dist, 0), tilt, np.max(touch, 0)


def events(eid):
    out = []
    for e in rows[eid]["events"].split("; "):
        if e:
            out.append((int(e.split(" ", 1)[0]), e.split(" ", 2)[1]))
    return out


timed = sorted(e for e, t in T["50%"].items() if t not in (None, 0))
kind, kind_first = {}, {}
for e in timed:
    ev = events(e)
    after = [k for s, k in ev if s >= T["50%"][e]]
    kind[e] = after[0] if after else "none"
    kind_first[e] = ev[0][1] if ev else "none"
lines = ["# Patterns at t_pnr", "", __doc__.split("\n\n")[0].replace("\n", " "), "",
         "Failure threshold 50%. Natural + perturbed pooled.", "", "| type | first event at or after t_pnr | first event of the run | median t_pnr | median event - t_pnr |",
         "|---|---|---|---|---|"]
for k in TYPES:
    es = [e for e in timed if kind[e] == k]
    gaps = [next(s for s, n in events(e) if s >= T["50%"][e]) - T["50%"][e] for e in es] if k != "none" else []
    lines.append(f"| {k} | {len(es)} | {sum(v == k for v in kind_first.values())} | {np.median([T['50%'][e] for e in es]) if es else 0:.0f} | "
                 + (f"{np.median(gaps):+.0f}" if gaps else "none") + " |")

rel = np.arange(-200, 101, 8)
sig = {}
for e in timed:
    q, dist, tilt, touch = signals(e)
    r = q - T["50%"][e]
    sig[e] = {n: np.interp(rel, r, v, left=np.nan, right=np.nan) for n, v in (("gripper distance (m)", dist), ("tilt (rad)", tilt), ("contact", touch))}
fig, axes = plt.subplots(3, 1, figsize=(9, 9), sharex=True)
for ax, n in zip(axes, ("gripper distance (m)", "tilt (rad)", "contact")):
    for k in TYPES:
        es = [e for e in timed if kind[e] == k]
        if len(es) < 3:
            continue
        m = np.stack([sig[e][n] for e in es])
        enough = (~np.isnan(m)).sum(0) >= 3
        with np.errstate(all="ignore"):
            med = np.nanmean(m, 0) if n == "contact" else np.nanmedian(m, 0)
        ax.plot(rel[enough], med[enough], label=f"{k} ({len(es)})")
        if n != "contact":
            lo, hi = np.nanpercentile(m, [25, 75], axis=0)
            ax.fill_between(rel[enough], lo[enough], hi[enough], alpha=0.12)
    ax.axvline(0, color="k", lw=1)
    ax.set_ylabel(n + (" (fraction of runs)" if n == "contact" else ""))
axes[0].legend(fontsize=8)
axes[2].set_xlabel("steps relative to t_pnr (failure threshold 50%)")
fig.tight_layout()
fig.savefig(os.path.join(args.out, "signals_by_type.png"), dpi=130)

lines += ["", "## First contact with a goal object vs t_pnr (timed failures of each threshold)", "",
          "| threshold | type (50% split) | before t_pnr | at or after t_pnr | never | median contact - t_pnr |", "|---|---|---|---|---|---|"]
for name, t in T.items():
    es_all = [e for e, v in t.items() if v not in (None, 0)]
    for k in TYPES + ["all"]:
        es = [e for e in es_all if k == "all" or kind.get(e) == k]
        if not es:
            continue
        gap = []
        for e in es:
            q, _, _, touch = signals(e)
            hit = np.nonzero(touch > 0)[0]
            gap.append(int(q[hit[0]]) - t[e] if len(hit) else None)
        real = [g for g in gap if g is not None]
        lines.append(f"| {name} | {k} | {sum(g < 0 for g in real)} | {sum(g >= 0 for g in real)} | {len(gap) - len(real)} | "
                     + (f"{np.median(real):+.0f}" if real else "none") + " |")
os.makedirs(args.out, exist_ok=True)
open(os.path.join(args.out, "patterns.md"), "w").write("\n".join(lines) + "\n")
print("\n".join(lines))
pick, by = [], {k: [e for e in timed if kind[e] == k] for k in TYPES}
while len(pick) < min(10, len(timed)):
    for k in TYPES:
        if by[k] and len(pick) < 10:
            pick.append(by[k].pop(0))
open(os.path.join(args.out, "clip_ids.txt"), "w").write("".join(f"{e} {T['50%'][e]} {kind[e]}\n" for e in pick))
