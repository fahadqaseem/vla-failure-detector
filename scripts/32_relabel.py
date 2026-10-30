"""t_pnr recomputed from the existing scans at failure thresholds 50, 70, 80% (Prof. Zhu meeting, Oct 30). Replay data only, no new runs.
Same failures as T1all (natural + perturbed + perturbed_v2, refined counts). A checkpoint is not recoverable if the raw failure
fraction is at least the threshold; t_pnr = first checkpoint from which every later one is not recoverable. With K = 4 that is
70% = 3 of 4 fail, 80% = 4 of 4 fail. 50% = the labels in use (Jeffreys tau 0.5), checked against T1all. Also shown: the Jeffreys rule
at tau 0.3 and 0.2. Pre-check failures have no scan and stay recoverable at every threshold. Timed = t_pnr > 0, doomed = t_pnr 0.

python scripts/32_relabel.py --out results/week3/relabel
"""

import argparse
import glob
import json
import os

import numpy as np
from scipy.stats import beta

p = argparse.ArgumentParser()
p.add_argument("--labels", default="results/week2/T1all_unseen_conv/per_episode.json")
p.add_argument("--out", default="results/week3/relabel")
args = p.parse_args()

scans = {}
for f in [f for pat in ("data/full_scans/*.json", "data/perturbed_scans/*.json", "data/perturbed_v2_scans/*.json") for f in glob.glob(pat)]:
    s = json.load(open(f))
    scans[s["episode_id"]] = s
for f in glob.glob("data/week2_refine/*.json"):
    r = json.load(open(f))
    s = scans[r["episode_id"]]
    for c, extra in zip(r["checkpoints"], r["successes"]):
        i = s["checkpoints"].index(c)
        s["successes"][i] = list(s["successes"][i]) + list(extra)


def t_pnr(scan, recoverable):
    ok = [recoverable(x) for x in scan["successes"]]
    if ok[-1]:
        return None
    i = len(ok) - 1
    while i > 0 and not ok[i - 1]:
        i -= 1
    return scan["checkpoints"][i]


jeff = lambda tau: (lambda x: beta.ppf(0.25, sum(x) + 0.5, len(x) - sum(x) + 0.5) >= tau)  # noqa: E731
raw = lambda thr: (lambda x: 1 - sum(x) / len(x) < thr)  # noqa: E731
RULES = {"50% (labels in use)": jeff(0.5), "70% (3 of 4 fail)": raw(0.7), "80% (4 of 4 fail)": raw(0.8),
         "Jeffreys tau 0.3": jeff(0.3), "Jeffreys tau 0.2": jeff(0.2)}
fails = [r for r in json.load(open(args.labels)) if r["model"] == "progress" and not r["success"]]
ref = {r["eid"]: r["t_pnr"] for r in fails}
table, per = [], {}
for name, rule in RULES.items():
    t = {e: t_pnr(scans[e], rule) if e in scans else None for e in ref}
    per[name] = t
    if name.startswith("50%"):
        bad = [e for e in ref if t[e] != ref[e]]
        assert not bad, f"50% does not reproduce T1all: {bad[:5]}"
    row = [name]
    for src, keep in (("all", lambda e: True), ("natural", lambda e: "_p" not in e), ("perturbed", lambda e: "_p" in e)):
        v = [t[e] for e in ref if keep(e)]
        row += [sum(x not in (None, 0) for x in v), sum(x == 0 for x in v), sum(x is None for x in v)]
    both = [t[e] - ref[e] for e in ref if t[e] not in (None, 0) and ref[e] not in (None, 0)]
    row += [len(both), float(np.median(both)), float(np.percentile(both, 25)), float(np.percentile(both, 75)),
            sum(ref[e] not in (None, 0) and t[e] is None for e in ref), sum(ref[e] == 0 and t[e] not in (None, 0) for e in ref)]
    table.append(row)
lines = ["# t_pnr at other failure thresholds", "", __doc__.split("\n\n")[0].replace("\n", " "), "",
         "| rule | timed | doomed | recoverable | natural timed / doomed / recov | perturbed timed / doomed / recov | timed in both | median shift (steps) | 25 to 75% | timed -> recoverable | doomed -> timed |",
         "|---|---|---|---|---|---|---|---|---|---|---|"]
for r in table:
    lines.append(f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} / {r[5]} / {r[6]} | {r[7]} / {r[8]} / {r[9]} | {r[10]} | {r[11]:+.0f} | {r[12]:+.0f} to {r[13]:+.0f} | {r[14]} | {r[15]} |")
os.makedirs(args.out, exist_ok=True)
open(os.path.join(args.out, "relabel.md"), "w").write("\n".join(lines) + "\n")
json.dump(per, open(os.path.join(args.out, "t_pnr_per_rule.json"), "w"), indent=0)
print("\n".join(lines))
