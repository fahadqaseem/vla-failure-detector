"""Dense replay report (pnr_probe, Oct 28 2026): replay pass rates per episode class and the primary comparison.

Pass = all three replay rules (dense_replay.py: eef <= 10 mm, same outcome, goal objects <= 10 mm). Classes from the
labels of the full-data run (per_episode.json of pnr_probe/results/unseen_t1): successes, recoverable failures (labelled,
no t_pnr), timed failures (t_pnr > 0), doomed failures (t_pnr = 0); failures without a label are listed apart.
Bias check, written at the top: if timed failures pass more than 10 percentage points less often than successes
(or Fisher exact p < 0.05), the comparison is biased towards failures whose replay works.
Primary comparison (decided Oct 28): model (b) gru_phys vs progress, unseen tasks, fixed 2.5% threshold, timely with the
paired 95% bootstrap interval, taken from the 13_report.py table (unseen_report_fixed_0.025.md).

python pnr_probe/dense/report.py --dense pnr_probe/data/dense --labels pnr_probe/results/unseen_t1/per_episode.json \
    --episodes pnr_probe/dense/all_episodes.txt --results pnr_probe/results/dense --out pnr_probe/results/dense/summary.md
"""

import argparse
import json
import os

import numpy as np
from scipy.stats import fisher_exact

p = argparse.ArgumentParser()
p.add_argument("--dense", required=True)
p.add_argument("--labels", required=True)
p.add_argument("--episodes", required=True)
p.add_argument("--results", required=True)
p.add_argument("--out", required=True)
p.add_argument("--pass_only", action="store_true", help="only the pass-rate table (gate before training)")
p.add_argument("--timed_rate_out", default=None, help="write the timed-failure pass rate (0 to 1) to this file")
args = p.parse_args()

lab = {r["eid"]: r for r in json.load(open(args.labels)) if r["model"] == "progress"}
eids = [os.path.splitext(os.path.basename(f.strip()))[0] for f in open(args.episodes) if f.strip()]


def klass(eid, success):
    if success:
        return "successes"
    r = lab.get(eid)
    if r is None:
        return "unlabelled failures"
    return "recoverable failures" if r["t_pnr"] is None else ("doomed failures" if r["t_pnr"] == 0 else "timed failures")


stats, missing = {}, []
for eid in eids:
    f = os.path.join(args.dense, eid + ".npz")
    if not os.path.exists(f):
        missing.append(eid)
        continue
    z = np.load(f)
    c = klass(eid, bool(z["success"]))
    s = stats.setdefault(c, np.zeros(5, int))  # n, passed, eef ok, outcome ok, objects ok
    s += [1, bool(z["passed"]), bool(z["pass_eef"]), bool(z["pass_outcome"]), bool(z["pass_obj"])]

top = []
if "timed failures" in stats and "successes" in stats:
    (nt, pt), (ns, ps) = stats["timed failures"][:2], stats["successes"][:2]
    gap, pv = ps / ns - pt / nt, fisher_exact([[pt, nt - pt], [ps, ns - ps]])[1]
    if gap > 0.10 or (pv < 0.05 and gap > 0):
        top = [f"**WARNING: timed failures pass the replay check much less often than successes ({pt}/{nt} = {pt / nt:.1%} vs "
               f"{ps}/{ns} = {ps / ns:.1%}, Fisher p = {pv:.3g}). Leaving out failed replays biases the comparison towards "
               "failures whose replay works.**", ""]
    else:
        top = [f"Bias check: timed failures pass {pt}/{nt} ({pt / nt:.1%}), successes {ps}/{ns} ({ps / ns:.1%}), Fisher p = "
               f"{pv:.3g}: no large gap (rule: more than 10 points lower, or p < 0.05).", ""]

lines = ["# Dense replay features: summary", ""] + top
if args.timed_rate_out and "timed failures" in stats:
    open(args.timed_rate_out, "w").write(f"{stats['timed failures'][1] / stats['timed failures'][0]:.4f}\n")
prim = None
rep = os.path.join(args.results, "unseen_report_fixed_0.025.md")
if os.path.exists(rep):
    for line in open(rep):
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(c) == 9 and c[0].endswith("unseen_b") and c[1] == "gru_phys":
            prim = c
        if len(c) == 9 and c[0].endswith("unseen_b") and c[1] == "progress":
            prog = c
if not args.pass_only:
    lines += ["## Primary comparison: (b) gru_phys vs progress, unseen tasks, 2.5% false alarms", ""]
if args.pass_only:
    pass
elif prim:
    lines += ["| model | timely (95% interval) | vs progress (paired 95% interval) | late / missed | median window | "
              "false alarms on successes | natural / perturbed |", "|---|---|---|---|---|---|---|",
              f"| (b) gru_phys | {prim[2]} | {prim[4]} | {prim[3]} | {prim[5]} | {prim[6]} | {prim[8]} |",
              f"| progress | {prog[2]} | | {prog[3]} | {prog[5]} | {prog[6]} | {prog[8]} |", ""]
else:
    lines += ["Run (b) unseen missing: training job failed or did not finish.", ""]
lines += ["## Replay pass rate (all three rules)", "",
          "| class | episodes | pass (all 3) | eef <= 10 mm | same outcome | goal objects <= 10 mm |", "|---|---|---|---|---|---|"]
order = ["successes", "recoverable failures", "timed failures", "doomed failures", "unlabelled failures"]
tot = np.zeros(5, int)
for c in order:
    if c in stats:
        s = stats[c]
        tot += s
        lines.append(f"| {c} | {s[0]} | {s[1]} ({s[1] / s[0]:.1%}) | {s[2]} | {s[3]} | {s[4]} |")
lines.append(f"| all | {tot[0]} | {tot[1]} ({tot[1] / max(tot[0], 1):.1%}) | {tot[2]} | {tot[3]} | {tot[4]} |")
if missing:
    lines += ["", f"No dense replay file (replay job failed): {len(missing)} episodes, e.g. {', '.join(missing[:5])}"]
lines += ["", "Secondary: (a) Track 1 physical + old micro-events, CUSUM variants, seen split and 5%: "
          "unseen_report_fixed_*.md, seen_report_fixed_*.md, ranking.md. All runs use only episodes that passed."]
open(args.out, "w").write("\n".join(lines) + "\n")
print("\n".join(lines))
