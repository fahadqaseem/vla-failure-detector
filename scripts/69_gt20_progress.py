"""Progress of the 20-replay full run (results/plan_nov22_gt20.md, amendment). Login node is fine: JSON and npz headers only.

Checkpoints done out of total (every 8 steps of every target run), replays in the files, new replays and GPU seconds in the last
--hours, and the projected GPU hours left: per missing checkpoint, new replays = 20 - reusable (pilot file: 0), each costing
a + b x the mean recorded replay length there (pilot fit, results/gt20/cost.md), scaled by actual / projected on the done checkpoints.

python scripts/69_gt20_progress.py --out results/gt20/progress.md
"""

import argparse
import glob
import json
import os
import time
from collections import Counter, defaultdict

import numpy as np

p = argparse.ArgumentParser()
p.add_argument("--targets", default="results/gt20/targets_oft.txt")
p.add_argument("--done", default="data/gt20/oft")
p.add_argument("--pilot", default="data/gt20_pilot")
p.add_argument("--scans", nargs="+", default=["data/full_scans/*.json", "data/perturbed_scans/*.json", "data/perturbed_v2_scans/*.json"])
p.add_argument("--refine", default="data/week2_refine")
p.add_argument("--a", type=float, default=1.65)
p.add_argument("--b", type=float, default=0.0288)
p.add_argument("--hours", type=float, default=12)
p.add_argument("--out", default="results/gt20/progress.md")
args = p.parse_args()
now = time.time()

scans = {}
for f in [f for g in args.scans for f in glob.glob(g)]:
    s = json.load(open(f))
    if "successes" in s and s["params"].get("noise_std") == 0.05:
        scans[s["episode_id"]] = s
extra = defaultdict(dict)
for f in glob.glob(os.path.join(args.refine, "*.json")):
    r = json.load(open(f))
    for c, e in zip(r["checkpoints"], r["end_steps"]):
        extra[r["episode_id"]][int(c)] = e

tot = done = runs_done = runs_started = n_left = 0
proj_done = proj_left = act_done = 0.0
n_new = n_reused = n_recent = s_recent = 0
gpus = Counter()
eids = [os.path.splitext(os.path.basename(x.strip()))[0] for x in open(args.targets) if x.strip()]
for eid in eids:
    s = scans[eid]
    d_run = n_run = 0
    for c, ends in zip(s["checkpoints"], s["end_steps"]):
        c = int(c)
        if c % 8:
            continue
        n_run += 1
        ends = list(ends) + list(extra[eid].get(c, []))
        need = 0 if os.path.exists(os.path.join(args.pilot, eid, f"c{c:03d}.json")) else max(20 - len(ends), 0)
        sec = need * (args.a + args.b * np.mean([e - c for e in ends]))
        f = os.path.join(args.done, eid, f"c{c:03d}.json")
        if not os.path.exists(f):
            proj_left += sec
            n_left += need
            continue
        d_run += 1
        r = json.load(open(f))
        new = [x for x in r["replays"] if x["source"] == "new"]
        n_new += len(new)
        n_reused += len(r["replays"]) - len(new)
        gpus.update(x["gpu"] for x in r["replays"])
        proj_done += sec
        act_done += sum(x["seconds"] for x in new)
        if now - os.path.getmtime(f) <= args.hours * 3600:
            n_recent += len(new)
            s_recent += sum(x["seconds"] for x in new)
    tot += n_run
    done += d_run
    runs_done += d_run == n_run
    runs_started += d_run > 0

ratio = act_done / proj_done if proj_done else 1.0
left_h = proj_left * ratio / 3600
busy = s_recent / (args.hours * 3600)
lines = [f"# 20-replay full run, progress ({time.strftime('%Y-%m-%d %H:%M')})", "",
         f"- Checkpoints: {done} of {tot} ({100 * done / tot:.1f}%); runs complete {runs_done} of {len(eids)}, started {runs_started}.",
         f"- Replays in the files: {n_new + n_reused} ({n_new} new, {n_reused} reused); GPU per replay: {dict(gpus)}.",
         f"- Last {args.hours:.0f} h: {n_recent} new replays ({n_recent / args.hours:.0f} per hour), {s_recent / 3600:.1f} GPU hours "
         f"(= {busy:.2f} GPUs busy on average).",
         f"- Done checkpoints: {act_done / 3600:.0f} GPU h actual vs {proj_done / 3600:.0f} projected (x {ratio:.2f}).",
         f"- Left: {n_left} new replays, about {left_h:.0f} GPU h (projection x {ratio:.2f}): "
         + ", ".join(f"{left_h / g / 24:.1f} days on {g} GPUs" for g in (2, 5)) + "."]
os.makedirs(os.path.dirname(args.out), exist_ok=True)
open(args.out, "w").write("\n".join(lines) + "\n")
print("\n".join(lines))
