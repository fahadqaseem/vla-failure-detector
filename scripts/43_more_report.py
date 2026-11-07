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

lines = ["| set | folder | gate | episodes | failures | scanned | timed t_pnr | doomed | recoverable |", "|---|---|---|---:|---:|---:|---:|---:|---:|"]
total = 0
for kind, scans in (("natural", "full_scans"), ("perturbed", "perturbed_scans"), ("perturbed_l2", "perturbed_l2_scans")):
    t = [0] * 6
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
        c = [len(rows), len(fails), len(pnr), sum(x is not None and x > 0 for x in pnr), sum(x == 0 for x in pnr), sum(x is None for x in pnr)]
        gate = "pass" if os.path.exists(d + "/GATE_PASS") else "FAIL" if os.path.exists(d + "/GATE_FAIL") else "none"
        lines.append(f"| {kind} | {os.path.basename(d)} | {gate} | " + " | ".join(map(str, c)) + " |")
        t = [a + b for a, b in zip(t, c)]
    lines.append(f"| **{kind}** | all | | " + " | ".join(map(str, t)) + " |")
    total += t[2]
os.makedirs(f"results/{args.policy}", exist_ok=True)
open(f"results/{args.policy}/more_failures.md", "w").write("\n".join(lines) + "\n")
print("\n".join(lines))
print(total)
