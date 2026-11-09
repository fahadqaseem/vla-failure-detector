"""Pi0.5 failure collection (Fahad, Nov 2): per folder, level 1 and level 2 apart, episodes, failures, scans. Last line printed = scanned failures,
natural + perturbed + level 2, which t2_more.sbatch reads.

python scripts/43_more_report.py --policy pi05
"""

import argparse
import csv
import glob
import json
import os

p = argparse.ArgumentParser()
p.add_argument("--policy", default="pi05")
args = p.parse_args()
base = f"data/{args.policy}"

lines = ["| set | folder | gate | episodes | failures | scanned | timed t_pnr | doomed | recoverable (scanned) | recoverable by pre-check (not scanned) |",
         "|---|---|---|---:|---:|---:|---:|---:|---:|---:|"]
total = 0
for kind, scans in (("natural", "full_scans"), ("perturbed", "perturbed_scans"), ("perturbed_l2", "perturbed_l2_scans")):
    t = [0] * 7
    for d in sorted(glob.glob(f"{base}/{kind}/task*")):
        if not os.path.exists(d + "/index.csv"):
            continue
        rows = [r for r in csv.DictReader(open(d + "/index.csv")) if r.get("success") not in (None, "")]  # skip a row being written (Nov 7)
        fails = [r["episode_id"] for r in rows if int(r["success"]) == 0]
        pnr = []
        for e in fails:
            f = f"{base}/{scans}/{e}.json"
            if os.path.exists(f):
                pnr.append(json.load(open(f))["t_pnr"])
        pre = 0
        for e in fails:
            f = f"{base}/{kind}/prechecks/{e}.json"
            pre += os.path.exists(f) and json.load(open(f))["verdict"].startswith("recoverable") and os.path.exists(d + "/GATE_PASS")
        c = [len(rows), len(fails), len(pnr), sum(x is not None and x > 0 for x in pnr), sum(x == 0 for x in pnr), sum(x is None for x in pnr), pre]
        gate = "pass" if os.path.exists(d + "/GATE_PASS") else "FAIL" if os.path.exists(d + "/GATE_FAIL") else "none"
        lines.append(f"| {kind} | {os.path.basename(d)} | {gate} | " + " | ".join(map(str, c)) + " |")
        t = [a + b for a, b in zip(t, c)]
    lines.append(f"| **{kind}** | all | | " + " | ".join(map(str, t)) + " |")
    total += t[2]
os.makedirs(f"results/{args.policy}", exist_ok=True)
note = ["", "Counting (Nov 9): \"scanned\" (the 40 and 70 targets) counts failures with a full replay scan only. A failure whose pre-check says",
        "recoverable (3 or more of 4 retries succeed near the end) gets no scan: it is labelled recoverable (0 at every step) but is not in the",
        "scanned count, so it appears in the last column, not under \"recoverable (scanned)\". The old Pi0.5 total of 44 failures",
        "(results/pi05/relabel) = 40 scanned + 4 recoverable by pre-check (seeds 0 and 1), and its 7 recoverable = 3 scanned natural failures",
        "with no t_pnr + those 4. Same rule (tau 0.5), different counting; nothing was relabelled. Seed 4 failures past the 70th were",
        "pre-checked but not scanned (the chain stops at 70), so they have no label and are left out of training and evaluation.",
        "data/pi05/perturbed/task05_s3 (13 episodes, index.csv without header after a reqp requeue, no gate) is left out everywhere."]
open(f"results/{args.policy}/more_failures.md", "w").write("\n".join(lines + note) + "\n")
print("\n".join(lines + note))
print(total)
