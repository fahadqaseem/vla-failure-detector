"""Best variant of each Phase C family for Phase D (rule fixed in docs/PLAN_week2.md before any result, Oct 23):
most timely alarms on unseen tasks at fixed 5%, among variants with held-out false alarms <= 6%; ties go to fewer
false alarms; if none qualifies, the variant with the fewest false alarms. Prints the chosen model names.

python scripts/17_pick_best.py --pred results/week2/C_unseen_rescue results/week2/C_unseen_memory --out results/week2/C_best.md
"""

import argparse
import json
import os

import numpy as np

p = argparse.ArgumentParser()
p.add_argument("--pred", nargs="+", required=True)
p.add_argument("--key", default="fixed 0.05")
p.add_argument("--max_fa", type=float, default=0.06)
p.add_argument("--out", required=True)
args = p.parse_args()

FAMILIES = {"rescue": ["mlp_rescue", "combined_rescue", "mlp_rescue_cusum", "combined_rescue_cusum"],
            "memory": ["gru", "conv", "gru_cusum", "conv_cusum"]}
rows = [r for d in args.pred for r in json.load(open(os.path.join(d, "per_episode.json")))]
lines, chosen = [f"# Best Phase C variant per family ({args.key}, false alarms <= {args.max_fa})", ""], []
for fam, names in FAMILIES.items():
    stats = []
    for m in names:
        mine = [r for r in rows if r["model"] == m]
        if not mine:
            continue
        timely = sum(r["alarms"][args.key] is not None and r["alarms"][args.key] <= r["t_pnr"]
                     for r in mine if not r["success"] and r["t_pnr"] not in (None, 0))
        fa = float(np.mean([r["alarms"][args.key] is not None for r in mine if r["success"]]))
        stats.append((m, timely, fa))
        lines.append(f"- {fam}: {m} timely {timely}, false alarms {fa:.3f}")
    ok = [s for s in stats if s[2] <= args.max_fa]
    best = (max(ok, key=lambda s: (s[1], -s[2])) if ok else min(stats, key=lambda s: s[2])) if stats else None
    if best:
        chosen.append(best[0])
        lines.append(f"- {fam}: CHOSEN {best[0]}" + ("" if ok else " (none within the false-alarm limit)"))
open(args.out, "w").write("\n".join(lines) + "\n")
print(" ".join(chosen))
