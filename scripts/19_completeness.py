"""What succeeded and what is missing in week 2 Phase A and B (Fahad, Oct 23): goes at the top of the Phase D report.

Slurm job states (sacct since --since, by job name) and file counts: collection per task, replay gate, pre-checks,
scans, K 16 refinement, look-ahead. Lists the missing episodes and tasks.

python scripts/19_completeness.py --out results/week2/D_completeness.md
"""

import argparse
import collections
import csv
import glob
import json
import os
import subprocess

p = argparse.ArgumentParser()
p.add_argument("--since", default="2026-10-23")
p.add_argument("--out", default="results/week2/D_completeness.md")
args = p.parse_args()

TASKS = [0, 1, 4, 5, 6, 7, 8]
stem = lambda f: os.path.splitext(os.path.basename(f))[0]  # noqa: E731
lines = ["# Week 2 completeness (Phase A and B)", ""]

# Slurm: array tasks per job name and state
out = subprocess.run(["sacct", "-S", args.since, "-n", "-P", "-o", "JobName,State",
                      "--name=w2-collect,w2-precheck,w2-scan,w2-refine,w2-lookahead"], capture_output=True, text=True).stdout
states = collections.defaultdict(collections.Counter)
for line in out.splitlines():
    name, state = line.split("|")[:2]
    if name in ("batch", "extern") or not name:
        continue
    states[name][state.split()[0]] += 1
lines.append("Slurm jobs (array tasks, including resubmits): " + "; ".join(
    f"{n}: {c['COMPLETED']} completed, {sum(v for s, v in c.items() if s != 'COMPLETED')} other"
    + (f" ({', '.join(f'{s} {v}' for s, v in c.items() if s != 'COMPLETED')})" if len(c) > 1 or 'COMPLETED' not in c else "")
    for n, c in sorted(states.items())))
lines.append("")

# Collection and gate per task
gate_pass = []
lines += ["| task | episodes (of 100) | failures | replay gate | pre-checks (of failures) | scan / recoverable |", "|---|---|---|---|---|---|"]
missing_pre = []
for t in TASKS:
    d = f"data/perturbed_v2/task{t:02d}"
    rows = list(csv.DictReader(open(f"{d}/index.csv"))) if os.path.exists(f"{d}/index.csv") else []
    fails = [r["episode_id"] for r in rows if int(r["success"]) == 0]
    gate = "pass" if os.path.exists(f"{d}/GATE_PASS") else ("FAIL: " + open(f"{d}/GATE_FAIL").read().strip()
                                                           if os.path.exists(f"{d}/GATE_FAIL") else "not run")
    pre = {e: json.load(open(f"data/perturbed_v2/prechecks/{e}.json"))["verdict"] for e in fails
           if os.path.exists(f"data/perturbed_v2/prechecks/{e}.json")}
    if gate == "pass":
        gate_pass.append(t)
        missing_pre += [e for e in fails if e not in pre]
    n_scan = sum(v == "scan" for v in pre.values())
    lines.append(f"| {t} | {len(rows)} | {len(fails)} | {gate} | {len(pre)} of {len(fails)} | {n_scan} / {len(pre) - n_scan} |")
lines += ["", f"Tasks dropped (gate failed or not run): {[t for t in TASKS if t not in gate_pass] or 'none'}. "
          f"Tasks with fewer than 100 episodes: {[t for t in TASKS if len(glob.glob(f'data/perturbed_v2/task{t:02d}/*.npz')) < 100] or 'none'} "
          "(an initial state is skipped after 20 invalid perturbed starts)."]
lines.append(f"Failures without a pre-check (gate passed): {missing_pre or 'none'}")


def done_vs_targets(name, targets, outdir, ext):
    if not os.path.exists(targets):
        return f"{name}: no target list"
    want = [stem(line.split()[0]) for line in open(targets) if line.strip()]
    missing = [e for e in want if not os.path.exists(os.path.join(outdir, e + ext))]
    return f"{name}: {len(want) - len(missing)} of {len(want)} done; missing: {missing or 'none'}"


lines += [done_vs_targets("Full scans (new failures)", "results/week2/scans/targets.txt", "data/perturbed_v2_scans", ".json"),
          done_vs_targets("K 16 refinement", "results/week2/refine/targets.txt", "data/week2_refine", ".json"),
          done_vs_targets("Look-ahead (Phase B)", "results/week2/lookahead/targets.txt", "data/week2_lookahead", ".npz"),
          "Failures that are missing a scan or pre-check have no label and are left out of every Phase D number."]
text = "\n".join(lines) + "\n"
os.makedirs(os.path.dirname(args.out), exist_ok=True)
open(args.out, "w").write(text)
print(text)
