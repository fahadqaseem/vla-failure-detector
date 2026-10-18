"""Do full replay scans support binary search for t_pnr?

For each full scan (every checkpoint) and each rule, a checkpoint is "recoverable" or not:
  tau rules (RESCUE): Jeffreys lower 0.25 quantile of Beta(k + 1/2, K - k + 1/2) >= tau
  "fails every replay": recoverable unless all K replays fail
t_pnr (full scan) = first checkpoint from which every later checkpoint is not recoverable (None if the
last one is recoverable). Binary search assumes one switch from recoverable to not; we simulate it on
the same counts and check that it gives the same t_pnr. We also count "rebounds": recoverable
checkpoints that come after a non-recoverable one (these break the one-switch assumption).

python scripts/check_monotonic.py --scans "data/full_scans/*.json" --out results/full_scans
"""

import argparse
import glob
import json
import os
import shutil

from scipy.stats import beta

p = argparse.ArgumentParser()
p.add_argument("--scans", default="data/full_scans/*.json")
p.add_argument("--out", default="results/full_scans")
args = p.parse_args()


def recoverable(k, K, rule):
    if rule == "fails every replay":
        return k > 0
    return beta.ppf(0.25, k + 0.5, K - k + 0.5) >= rule


def t_pnr_full(ckpts, ok):
    if ok[-1]:
        return None
    i = len(ok) - 1
    while i > 0 and not ok[i - 1]:
        i -= 1
    return ckpts[i]


def t_pnr_binary(ckpts, ok):
    if ok[-1]:
        return None
    if not ok[0]:
        return ckpts[0]
    lo, hi = 0, len(ok) - 1  # ok[lo] is recoverable, ok[hi] is not
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if ok[mid]:
            lo = mid
        else:
            hi = mid
    return ckpts[hi]


os.makedirs(args.out, exist_ok=True)
rules = [0.3, 0.5, 0.7, "fails every replay"]
lines = ["# Full replay scans: does binary search find the same t_pnr?", "",
         "Natural failures, every checkpoint (8 steps), K = 4 at every checkpoint (no K = 16 expansion), "
         "noise 0.05 on 6 arm dims, extra_steps 200. Rule per checkpoint: Jeffreys lower 0.25 quantile >= tau, "
         "or 'fails every replay'.", ""]
lines.append("Jeffreys lower 0.25 quantile for k of 4 successes: "
             + ", ".join(f"k={k}: {beta.ppf(0.25, k + 0.5, 4 - k + 0.5):.3f}" for k in range(5)))
lines += ["", "| episode | rule | t_pnr full scan | t_pnr binary search | same | rebounds after first non-recoverable |",
          "|---|---|---|---|---|---|"]
for f in sorted(glob.glob(args.scans)):
    r = json.load(open(f))
    shutil.copy(f, args.out)
    ckpts, K = r["checkpoints"], r["params"]["K"]
    counts = [sum(x) for x in r["successes"]]
    for rule in rules:
        ok = [recoverable(k, K, rule) for k in counts]
        first_bad = ok.index(False) if False in ok else None
        rebounds = 0 if first_bad is None else sum(ok[first_bad:])
        full, bs = t_pnr_full(ckpts, ok), t_pnr_binary(ckpts, ok)
        name = f"tau {rule}" if rule != "fails every replay" else rule
        lines.append(f"| {r['episode_id']} | {name} | {full} | {bs} | {full == bs} | {rebounds} |")
    lines.append(f"| {r['episode_id']} | successes of {K} per checkpoint | "
                 + " ".join(str(k) for k in counts) + " | | | |")

text = "\n".join(lines) + "\n"
open(os.path.join(args.out, "summary.md"), "w").write(text)
print(text)
