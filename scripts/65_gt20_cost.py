"""Cost plan for a 20-replay ground truth (results/plan_nov22_gt20.md, Step 2). CPU, reads JSON only.

1. Time per replay from the pilot (data/gt20_pilot, new replays only): successful vs failed, and a least-squares fit
   seconds = a + b x replay steps (steps = end step - checkpoint).
2. The same fit from the existing K 4 scans (minutes per scan vs number of replays and their total steps): OFT as a cross-check,
   Pi0.5 as its only source (no Pi0.5 pilot this week).
3. Projection per design from the replay lengths recorded in the existing scans (end_steps, every 8 steps): at each chosen checkpoint
   new replays = K - reusable (4 from the scan, plus refinement replays where present), each costing a + b x the mean recorded length there.
   Runs = kept failed runs of results/regression_v2 (OFT 136, Pi0.5 37), or 50 OFT runs (round robin over tasks, lowest id first).
   Adaptive: K 20 only where the 4-replay failure fraction is in [0.25, 0.75] or differs by 0.5 or more from a neighbouring checkpoint of
   the same grid (a change), K 4 (nothing new) elsewhere.
Days = GPU hours / (24 x GPUs at once).

python scripts/65_gt20_cost.py --out results/gt20/cost.md
"""

import argparse
import glob
import json
import os
from collections import defaultdict

import numpy as np

p = argparse.ArgumentParser()
p.add_argument("--pilot", default="data/gt20_pilot")
p.add_argument("--out", default="results/gt20/cost.md")
p.add_argument("--gpus", type=int, default=5)
p.add_argument("--days", type=float, default=10)
args = p.parse_args()

SCANS = {"oft": ["data/full_scans/*.json", "data/perturbed_scans/*.json", "data/perturbed_v2_scans/*.json"],
         "pi05": ["data/pi05/full_scans/*.json", "data/pi05/perturbed_scans/*.json"]}
REFINE = {"oft": "data/week2_refine", "pi05": None}
NAMES = {"oft": "OpenVLA-OFT", "pi05": "Pi0.5"}


def fit(x_steps, n_rep, secs):
    """secs = a x n_rep + b x steps (least squares, no intercept: n_rep carries the per-replay overhead)."""
    A = np.c_[n_rep, x_steps].astype(float)
    (a, b), *_ = np.linalg.lstsq(A, np.asarray(secs, float), rcond=None)
    return float(a), float(b)


# ---- 1. pilot ----
pilot = [json.load(open(f)) for f in sorted(glob.glob(os.path.join(args.pilot, "*", "c*.json")))]
new = [(r["end_step"] - c["checkpoint"], r["seconds"], r["success"]) for c in pilot for r in c["replays"] if r["source"] == "new"]
lines = ["# Cost plan for a 20-replay ground truth (plan: results/plan_nov22_gt20.md, Step 2)", ""]
if new:
    steps, secs, ok = map(np.array, zip(*new))
    a_p, b_p = fit(steps, np.ones(len(steps)), secs)
    lines += [f"## Time per replay, OpenVLA-OFT pilot ({len(pilot)} checkpoints done, {len(new)} new replays, galhp L40S)", "",
              "| replays | n | mean seconds | median | mean steps |", "|---|---|---|---|---|"]
    for lab, m in (("successful", ok == 1), ("failed", ok == 0), ("all", ok >= 0)):
        if m.any():
            lines.append(f"| {lab} | {m.sum()} | {secs[m].mean():.1f} | {np.median(secs[m]):.1f} | {steps[m].mean():.0f} |")
    lines += ["", f"Fit seconds = {a_p:.2f} + {b_p:.4f} x replay steps (a failed replay from step c runs 720 - c steps).", ""]
else:
    a_p = b_p = None
    lines += ["No pilot replays finished yet.", ""]

# ---- 2. existing scans ----
runs, scans_by = {}, {}
for pol in SCANS:
    scans = {}
    for f in [f for g in SCANS[pol] for f in glob.glob(g)]:
        s = json.load(open(f))
        scans[s["episode_id"]] = s
    extra = defaultdict(dict)
    if REFINE[pol]:
        for f in glob.glob(os.path.join(REFINE[pol], "*.json")):
            r = json.load(open(f))
            for c, s, e in zip(r["checkpoints"], r["successes"], r["end_steps"]):
                extra[r["episode_id"]][int(c)] = (s, e)
    scans_by[pol] = (scans, extra)
    rows = {}
    for f in glob.glob(f"data/regression_v2/{pol}/const/s0/g*.json"):
        for r in json.load(open(f))["rows"]:
            rows[r["eid"]] = r
    runs[pol] = sorted(e for e, r in rows.items() if not r["success"])

lines += ["## Time per replay from the existing K 4 scans (minutes per scan; fit seconds = a + b x steps)", "",
          "| policy | scans | a (s per replay) | b (s per step) | failed replay from step 0 (720 steps), s | mean scan minutes |",
          "|---|---|---|---|---|---|"]
coef = {}
for pol in SCANS:
    scans, _ = scans_by[pol]
    S = [s for s in scans.values() if "end_steps" in s and s.get("minutes")]
    st = [sum(e - c for c, es in zip(s["checkpoints"], s["end_steps"]) for e in es) for s in S]
    nr = [sum(len(es) for es in s["end_steps"]) for s in S]
    a, b = fit(st, nr, [s["minutes"] * 60 for s in S])
    coef[pol] = (a, b)
    lines.append(f"| {NAMES[pol]} | {len(S)} | {a:.2f} | {b:.4f} | {a + 720 * b:.0f} | {np.mean([s['minutes'] for s in S]):.0f} |")
if a_p is not None:
    coef["oft"] = (a_p, b_p)
    lines += ["", "OFT projections below use the pilot fit; Pi0.5 uses its scan fit (no Pi0.5 pilot this week)."]
else:
    lines += ["", "No pilot yet: both projections use the scan fits."]
lines.append("")

# ---- 3. designs ----
def run_cost(pol, eid, every, K, adaptive):
    scans, extra = scans_by[pol]
    s = scans[eid]
    a, b = coef[pol]
    cps = [int(c) for c in s["checkpoints"]]
    grid = [i for i, c in enumerate(cps) if c % every == 0]
    f4 = {i: 1 - sum(s["successes"][i]) / len(s["successes"][i]) for i in grid}
    secs, n_new = 0.0, 0
    for j, i in enumerate(grid):
        c = cps[i]
        if adaptive:
            nb = [f4[grid[m]] for m in (j - 1, j + 1) if 0 <= m < len(grid)]
            if not (0.25 <= f4[i] <= 0.75 or any(abs(f4[i] - v) >= 0.5 for v in nb)):
                continue
        ends = list(s["end_steps"][i]) + (list(extra[eid][c][1]) if c in extra[eid] else [])
        need = max(K - len(ends), 0)
        secs += need * (a + b * np.mean([e - c for e in ends]))
        n_new += need
    return secs, n_new


def fifty(eids):
    by = defaultdict(list)
    for e in sorted(eids):
        by[int(e[1:3])].append(e)
    out = []
    while len(out) < 50 and any(by.values()):
        for t in sorted(by):
            if by[t] and len(out) < 50:
                out.append(by[t].pop(0))
    return out


designs = []
for pol in ("oft", "pi05"):
    sets = [("all", runs[pol])] + ([("50", fifty(runs[pol]))] if pol == "oft" else [])
    for set_name, eids in sets:
        for every in (8, 16, 32):
            for K, adaptive in ((8, False), (20, False), (20, True)):
                tot = [run_cost(pol, e, every, K, adaptive) for e in eids]
                h = sum(t[0] for t in tot) / 3600
                designs.append(dict(pol=pol, set=set_name, n=len(eids), every=every, K=K, adaptive=adaptive, hours=h,
                                    replays=sum(t[1] for t in tot), days=h / 24 / args.gpus))
lines += [f"## Projected cost ({args.gpus} GPUs at once, all the time; real queue waits come on top)", "",
          "| policy | runs | every | design | new replays | GPU hours | days |", "|---|---|---|---|---|---|---|"]
lab = lambda d: "adaptive (K 20 where 0.25 <= f4 <= 0.75 or at a change)" if d["adaptive"] else f"K {d['K']}"  # noqa: E731
for d in designs:
    lines.append(f"| {NAMES[d['pol']]} | {d['n']} | {d['every']} | {lab(d)} | {d['replays']} | {d['hours']:.0f} | {d['days']:.1f} |")

# Recommendation: OFT design + Pi0.5 design sharing the GPUs, total within --days. Preference: K 20 full > adaptive > K 8, then more OFT
# runs, then a finer grid; Pi0.5 always all 37 runs with the same grid and design when it fits.
rank = lambda d: ({(20, False): 2, (20, True): 1}.get((d["K"], d["adaptive"]), 0), d["n"], -d["every"])  # noqa: E731
best = None
for d in sorted([d for d in designs if d["pol"] == "oft"], key=rank, reverse=True):
    pi = [x for x in designs if x["pol"] == "pi05" and x["every"] == d["every"] and x["K"] == d["K"] and x["adaptive"] == d["adaptive"]][0]
    if d["days"] + pi["days"] <= args.days:
        best = (d, pi)
        break
lines += ["", "## Recommendation", ""]
if best:
    d, pi = best
    lines.append(f"Largest design within about {args.days:.0f} days on {args.gpus} GPUs (preference: K 20 everywhere, then adaptive, then K 8; "
                 f"then more runs; then a finer grid; Pi0.5 with the same design): OpenVLA-OFT {d['n']} runs, every {d['every']}, {lab(d)}: "
                 f"{d['hours']:.0f} GPU h ({d['days']:.1f} days) + Pi0.5 {pi['n']} runs: {pi['hours']:.0f} GPU h ({pi['days']:.1f} days) = "
                 f"{d['days'] + pi['days']:.1f} days.")
else:
    lines.append(f"No design for both policies fits in {args.days:.0f} days on {args.gpus} GPUs.")
os.makedirs(os.path.dirname(args.out), exist_ok=True)
open(args.out, "w").write("\n".join(lines) + "\n")
print("\n".join(lines))
