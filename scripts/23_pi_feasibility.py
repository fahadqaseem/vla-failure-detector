"""Track 2 feasibility verdict (Oct 23 2026): success of 20 natural episodes per LIBERO-10 task (initial states 0-19)
against the published LIBERO-10 numbers. Rule fixed before the run: PASS if our overall success is within 10 points
of the reference number (our setting re-queries every 8 steps, so a few points of difference are expected).
References: pi0 85.2 (openpi README, pi0 @ 30k finetuned, Jul 2025); pi05 92.4 (Fahad, Oct 30; LeRobot docs give 96.0 for its port;
that is not the reference).

python scripts/23_pi_feasibility.py --policy pi0
"""

import argparse
import csv
import glob
import json
import os

import numpy as np

p = argparse.ArgumentParser()
p.add_argument("--policy", required=True, choices=["pi0", "pi05"])
p.add_argument("--max_gap", type=float, default=10.0)
args = p.parse_args()
REF = {"pi0": (85.2, "openpi README, pi0 @ 30k finetuned"), "pi05": (92.4, "openpi pi05_libero; LeRobot reports 96.0 for its port")}

rows = [r for f in sorted(glob.glob(f"data/{args.policy}/natural/task*/index.csv")) for r in csv.DictReader(open(f))
        if int(r["episode_idx"]) < 20]
lines = [f"# {args.policy} feasibility: 20 natural episodes per LIBERO-10 task (initial states 0-19)", "",
         "| task | episodes | successes | rate |", "|---|---|---|---|"]
for t in range(10):
    rs = [r for r in rows if int(r["task_id"]) == t]
    k = sum(int(r["success"]) for r in rs)
    lines.append(f"| {t} | {len(rs)} | {k} | {100 * k / len(rs):.0f}% |" if rs else f"| {t} | 0 | 0 | none |")
n, k = len(rows), sum(int(r["success"]) for r in rows)
rate = 100 * k / n if n else float("nan")
z = 1.96  # Wilson 95% interval
lo, hi = [(100 * (k / n + z * z / (2 * n) + s * z * np.sqrt(k / n * (1 - k / n) / n + z * z / (4 * n * n))) / (1 + z * z / n))
          for s in (-1, 1)] if n else (np.nan, np.nan)
ref, src = REF[args.policy]
verdict = "PASS" if n >= 190 and abs(rate - ref) <= args.max_gap else "FAIL"
checks = json.load(open(f"results/{args.policy}/checks.json")) if os.path.exists(f"results/{args.policy}/checks.json") else {}
lines += ["", f"Overall: {k} of {n} = {rate:.1f}% (Wilson 95% {lo:.1f} to {hi:.1f}); reference {ref} ({src}). "
          f"Rule: within {args.max_gap:.0f} points and at least 190 episodes. Verdict: {verdict}.",
          f"Checks (22_pi_checks.py): {json.dumps(checks)}"]
os.makedirs(f"results/{args.policy}", exist_ok=True)
open(f"results/{args.policy}/feasibility.md", "w").write("\n".join(lines) + "\n")
open(f"results/{args.policy}/feasibility_status.txt", "w").write(f"{verdict} {rate:.1f}% of {n} (ref {ref})\n")
print("\n".join(lines))
