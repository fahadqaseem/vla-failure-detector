"""Old vs new t_pnr labels for the same episodes (Oct 19 2026: rescan with restore_query).

t_pnr rule as in 06_train_predictor.py: K 4, tau 0.5 (recoverable if >= 3 of 4 replays succeed); t_pnr = first
checkpoint from which every later checkpoint is not recoverable, None if the last one is recoverable.

python scripts/compare_labels.py --old "data/full_scans_oct18_restore/*.json" --new "data/full_scans/*.json" \
    --out results/full_scans/rescan_compare.md
"""

import argparse
import glob
import json

import numpy as np

p = argparse.ArgumentParser()
p.add_argument("--old", required=True)
p.add_argument("--new", required=True)
p.add_argument("--out", required=True)
p.add_argument("--tau_min_success", type=int, default=3)
args = p.parse_args()


def t_pnr(scan):
    ok = [sum(s) >= args.tau_min_success for s in scan["successes"]]
    if ok[-1]:
        return None
    i = len(ok) - 1
    while i > 0 and not ok[i - 1]:
        i -= 1
    return scan["checkpoints"][i]


def load(pattern):
    return {s["episode_id"]: s for s in (json.load(open(f)) for f in glob.glob(pattern))}


old, new = load(args.old), load(args.new)
both = sorted(set(old) & set(new))
rows, changed, diffs = [], 0, []
for eid in both:
    a, b = t_pnr(old[eid]), t_pnr(new[eid])
    same_curve = old[eid]["successes"] == new[eid]["successes"]
    if a != b:
        changed += 1
        if a is not None and b is not None:
            diffs.append(abs(a - b))
    rows.append(f"| {eid} | {'success' if old[eid]['recorded_success'] else 'failure'} | {a} | {b} | "
                f"{'yes' if a != b else ''} | {'' if same_curve else 'differs'} |")
fails = [e for e in both if not old[e]["recorded_success"]]
kinds = {k: sum((t_pnr(old[e]) is None) == ko and (t_pnr(new[e]) is None) == kn and t_pnr(old[e]) != t_pnr(new[e])
                for e in both)
         for k, (ko, kn) in {"recoverable -> t_pnr": (True, False), "t_pnr -> recoverable": (False, True),
                             "t_pnr moved": (False, False)}.items()}
lines = ["# t_pnr before and after the restore fix", "",
         f"Old: `{args.old}` ({len(old)} scans). New: `{args.new}` ({len(new)} scans). In both: {len(both)} "
         f"({len(fails)} failures). Only in old: {sorted(set(old) - set(new)) or 'none'}. Only in new: {sorted(set(new) - set(old)) or 'none'}.",
         "", f"t_pnr changed: {changed} of {len(both)}. " + ", ".join(f"{k}: {v}" for k, v in kinds.items())
         + (f". Where both have a t_pnr, |change| median {np.median(diffs):.0f} steps, max {max(diffs)}." if diffs else "."),
         f"Replay success counts identical at every checkpoint: {sum(old[e]['successes'] == new[e]['successes'] for e in both)} of {len(both)}.",
         "", "| episode | recorded | old t_pnr | new t_pnr | changed | success counts |", "|---|---|---|---|---|---|"] + rows
open(args.out, "w").write("\n".join(lines) + "\n")
print("\n".join(lines[:6]))
