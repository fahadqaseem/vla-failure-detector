"""How many t_pnr values change when the K 16 boundary replays (data/week2_refine) are added (Oct 23).
K 4: recoverable if >= 3 of 4 succeed; refined: Jeffreys lower 0.25 quantile >= 0.5 (10 of 16). Same t_pnr rule.

python scripts/18_refine_changes.py --scans "data/full_scans/*.json" --refine data/week2_refine --out results/week2/refine_changes.md
"""

import argparse
import glob
import json
import os

from scipy.stats import beta

p = argparse.ArgumentParser()
p.add_argument("--scans", nargs="+", required=True)
p.add_argument("--refine", required=True)
p.add_argument("--out", required=True)
args = p.parse_args()


def t_pnr(checkpoints, successes):
    ok = [beta.ppf(0.25, sum(s) + 0.5, len(s) - sum(s) + 0.5) >= 0.5 for s in successes]
    if ok[-1]:
        return None
    i = len(ok) - 1
    while i > 0 and not ok[i - 1]:
        i -= 1
    return checkpoints[i]


lines = ["| episode | t_pnr K 4 | t_pnr K 16 at boundary |", "|---|---|---|"]
n = changed = 0
for f in sorted(glob.glob(os.path.join(args.refine, "*.json"))):
    r = json.load(open(f))
    s = next(json.load(open(g)) for pat in args.scans for g in glob.glob(pat) if os.path.basename(g) == os.path.basename(f))
    succ = [list(x) for x in s["successes"]]
    for c, extra in zip(r["checkpoints"], r["successes"]):
        succ[s["checkpoints"].index(c)] += list(extra)
    old, new = t_pnr(s["checkpoints"], s["successes"]), t_pnr(s["checkpoints"], succ)
    n += 1
    changed += old != new
    lines.append(f"| {r['episode_id']} | {old} | {new} |")
text = f"# K 16 refinement: {changed} of {n} refined episodes change t_pnr\n\n" + "\n".join(lines) + "\n"
open(args.out, "w").write(text)
print(text.splitlines()[0])
