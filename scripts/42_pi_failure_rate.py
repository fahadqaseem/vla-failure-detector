"""Pi0.5 perturbed failure rate per task and the episodes needed for a target number of scanned failures (Fahad, Nov 2).
Only tasks whose natural gate passed. "Scan" = failure with pre-check verdict scan, in a task whose perturbed gate passed.

python scripts/42_pi_failure_rate.py --have 20 --target 40
"""

import argparse
import csv
import glob
import json
import os

from scipy.stats import chi2

p = argparse.ArgumentParser()
p.add_argument("--have", type=int, default=20, help="scanned failures so far, natural + perturbed")
p.add_argument("--target", type=int, default=40)
p.add_argument("--out", default="results/pi05/failure_rate.md")
args = p.parse_args()

need = args.target - args.have
lines = ["| task | perturbed gate | episodes | failures | to scan | recoverable (pre-check) |", "|---|---|---:|---:|---:|---:|"]
all_n = all_f = pass_n = pass_scan = pass_f = gates = tasks = 0
for d in sorted(glob.glob("data/pi05/natural/task*")):
    if not os.path.exists(d + "/GATE_PASS"):
        continue
    pd = d.replace("natural", "perturbed")
    rows = list(csv.DictReader(open(pd + "/index.csv")))
    fails = [r["episode_id"] for r in rows if int(r["success"]) == 0]
    ok = os.path.exists(pd + "/GATE_PASS")
    verdict = []
    for e in fails:
        f = f"data/pi05/perturbed/prechecks/{e}.json"
        verdict.append(json.load(open(f))["verdict"] if os.path.exists(f) else "none")
    scan, rec = verdict.count("scan"), sum(v.startswith("recoverable") for v in verdict)
    lines.append(f"| {os.path.basename(pd)} | {'pass' if ok else 'FAIL'} | {len(rows)} | {len(fails)} | {scan} | {rec} |")
    tasks += 1
    gates += ok
    all_n += len(rows)
    all_f += len(fails)
    if ok:
        pass_n += len(rows)
        pass_f += len(fails)
        pass_scan += scan

rate = pass_scan / pass_n
low = chi2.ppf(0.025, 2 * pass_scan) / 2 / pass_n  # exact Poisson 95% interval on the count
high = chi2.ppf(0.975, 2 * (pass_scan + 1)) / 2 / pass_n
gate = gates / tasks
lines += ["",
          f"Need {need} more scanned failures ({args.have} now, target {args.target}).",
          f"All {tasks} tasks: {all_f} failures of {all_n} episodes ({all_f / all_n:.3f}).",
          f"Perturbed gate passed on {gates} of {tasks} tasks: {pass_scan} to scan of {pass_n} episodes, rate {rate:.4f} (95% {low:.4f} to {high:.4f}).",
          f"Episodes in gate-passed tasks: {need / rate:.0f} (95% {need / high:.0f} to {need / low:.0f}).",
          f"Episodes collected if {gates} of {tasks} tasks keep passing the gate: {need / rate / gate:.0f} (95% {need / high / gate:.0f} to {need / low / gate:.0f})."]
open(args.out, "w").write("\n".join(lines) + "\n")
print("\n".join(lines))
