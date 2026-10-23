"""K 16 near the tau 0.5 boundary (CLAUDE.md decision 1; rule fixed in docs/PLAN_week2.md, Oct 23).

For every scanned failure with t_pnr > 0 (K 4 full scan), the two checkpoints around the boundary are
t_pnr - 8 (last recoverable) and t_pnr. The boundary is "close to tau" if t_pnr - 8 has exactly 3 of 4 successes
or t_pnr has exactly 2 of 4. Those episodes get 12 more replays at both checkpoints (03_pnr_scan.py --K 12
--seed 1 --t_min t_pnr-8 --t_max t_pnr), one line "episode t_min t_max" each.

python scripts/15_refine_targets.py --scans "data/full_scans/*.json" --out results/week2/refine/targets.txt
"""

import argparse
import glob
import json
import os

p = argparse.ArgumentParser()
p.add_argument("--scans", nargs="+", required=True)
p.add_argument("--out", required=True)
args = p.parse_args()

episode_path = {os.path.splitext(os.path.basename(f))[0]: f for pat in
                ["data/natural/*/*.npz", "data/perturbed/*/*.npz", "data/perturbed_v2/*/*.npz"] for f in glob.glob(pat)}
lines, n_timed = [], 0
for f in sorted(f for pat in args.scans for f in glob.glob(pat)):
    s = json.load(open(f))
    if s["recorded_success"] or s["params"]["K"] != 4:
        continue
    k = [sum(x) for x in s["successes"]]
    ok = [x >= 3 for x in k]
    if ok[-1]:
        continue  # recoverable failure: no t_pnr
    i = len(ok) - 1
    while i > 0 and not ok[i - 1]:
        i -= 1
    if i == 0:
        continue  # doomed from start (t_pnr 0): no boundary
    n_timed += 1
    if k[i - 1] == 3 or k[i] == 2:
        lines.append(f"{episode_path[s['episode_id']]} {s['checkpoints'][i - 1]} {s['checkpoints'][i]}")
os.makedirs(os.path.dirname(args.out), exist_ok=True)
open(args.out, "w").write("".join(line + "\n" for line in lines))
print(f"{n_timed} timed failures, {len(lines)} close to tau -> {args.out}")
