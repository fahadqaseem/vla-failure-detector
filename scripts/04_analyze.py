"""Turn PNR scans into a table and figures for the meeting. Runs on CPU (login node is fine).

python scripts/04_analyze.py                                   # PNR only
python scripts/04_analyze.py --onsets onsets.csv --alarms alarms.csv
  onsets.csv: episode_id,t_onset   (human labels, policy-step units)
  alarms.csv: episode_id,t_alarm   (first alarm of a detector at a fixed threshold)
"""

import argparse
import csv
import glob
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

from pnr.pnr import classify_alarm, timeline_row, value_at, value_curve  # noqa: E402

p = argparse.ArgumentParser()
p.add_argument("--pnr_dir", default="data/pnr")
p.add_argument("--onsets", default=None)
p.add_argument("--alarms", default=None)
p.add_argument("--out", default="results")
args = p.parse_args()


def read_times(path, col):
    if not path:
        return {}
    with open(path) as fh:
        return {r["episode_id"]: int(float(r[col])) for r in csv.DictReader(fh) if r.get(col) not in (None, "")}


onsets, alarms = read_times(args.onsets, "t_onset"), read_times(args.alarms, "t_alarm")
scans = [json.load(open(f)) for f in sorted(glob.glob(os.path.join(args.pnr_dir, "*.json")))]
if not scans:
    sys.exit(f"no scans in {args.pnr_dir}")
os.makedirs(args.out, exist_ok=True)

rows = []
for s in scans:
    row = {"episode_id": s["episode_id"], "task_id": s["task_id"], "induced": s["induced"],
           "recorded_success": s["recorded_success"], "t_end": s["t_end"]}
    row.update(timeline_row(s["t_pnr"], alarms.get(s["episode_id"]), onsets.get(s["episode_id"])))
    row["value_at_alarm"] = value_at(s["checkpoints"], np.array(s["successes"]), row["t_alarm"])
    row["alarm_class"] = classify_alarm(row["t_alarm"], row["t_pnr"], row["t_onset"], row["value_at_alarm"],
                                        s["recorded_success"])
    rows.append(row)

with open(os.path.join(args.out, "pnr_table.csv"), "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0]))
    w.writeheader()
    w.writerows(rows)


def stats(key, subset):
    v = [r[key] for r in subset if r[key] is not None]
    return (len(v), float(np.median(v)) if v else None)


params = scans[0]["params"]
lines = [f"# PNR summary ({len(scans)} scanned episodes)", "",
         f"Estimator: every={params['every']} steps, K={params['K']}, min_fail={params['min_fail']}, "
         f"noise_std={params['noise_std']}. Natural and induced failures reported separately.", ""]
for label, subset in [("natural failures", [r for r in rows if not r["induced"] and not r["recorded_success"]]),
                      ("induced failures", [r for r in rows if r["induced"] and not r["recorded_success"]]),
                      ("successful controls", [r for r in rows if r["recorded_success"]])]:
    if not subset:
        continue
    n_pnr, med_pnr = stats("t_pnr", subset)
    lines.append(f"## {label}: {len(subset)} episodes")
    lines.append(f"- PNR found: {n_pnr}/{len(subset)}; median t_pnr = {med_pnr}")
    for key in ["t_onset", "t_alarm", "detection_window", "intervention_window"]:
        n, med = stats(key, subset)
        if n:
            lines.append(f"- {key}: n={n}, median {med}")
    classes = [r["alarm_class"] for r in subset if r["alarm_class"]]
    if classes:
        counts = {c: classes.count(c) for c in sorted(set(classes))}
        lines.append(f"- alarm classes: {counts}")
    lines.append("")
open(os.path.join(args.out, "pnr_summary.md"), "w").write("\n".join(lines))
print("\n".join(lines))

# Figure 1: risk curves (only meaningful for full-curve scans; backward scans show the scanned tail).
fig, ax = plt.subplots(figsize=(7, 4))
for s in scans:
    if s["recorded_success"]:
        continue
    risk = 1 - value_curve(np.array(s["successes"]))
    line, = ax.plot(s["checkpoints"], risk, marker="o", ms=3, lw=1.2, alpha=0.8,
                    ls="--" if s["induced"] else "-")
    if s["t_pnr"] is not None:
        ax.axvline(s["t_pnr"], color=line.get_color(), lw=0.8, alpha=0.5)
    if s["episode_id"] in onsets:
        ax.plot(onsets[s["episode_id"]], 1.02, marker="v", color=line.get_color())
ax.set_xlabel("policy step")
ax.set_ylabel("replay risk = 1 - success rate")
ax.set_ylim(-0.05, 1.08)
ax.set_title("Replay risk per failed episode (vertical line = t_pnr, triangle = human onset)")
fig.tight_layout()
fig.savefig(os.path.join(args.out, "risk_curves.png"), dpi=160)

# Figure 2: timeline per episode (PNR, alarm, onset, end).
fig, ax = plt.subplots(figsize=(7, 0.45 * len(rows) + 1.2))
labelled = set()
for i, r in enumerate(rows):
    ax.plot([0, r["t_end"]], [i, i], color="0.85", lw=4)
    for key, mk, col in [("t_pnr", "o", "C3"), ("t_alarm", "s", "C0"), ("t_onset", "v", "C2")]:
        if r[key] is not None:
            ax.plot(r[key], i, marker=mk, color=col, ms=7, ls="none", label=None if key in labelled else key)
            labelled.add(key)
ax.set_yticks(range(len(rows)), [r["episode_id"] for r in rows], fontsize=7)
ax.set_xlabel("policy step")
ax.legend(loc="lower right", fontsize=8)
ax.set_title("Two clocks: point of no return vs when failure is noticed")
fig.tight_layout()
fig.savefig(os.path.join(args.out, "timeline.png"), dpi=160)
print(f"wrote {args.out}/pnr_table.csv, pnr_summary.md, risk_curves.png, timeline.png")
