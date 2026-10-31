"""Do the detectors catch different failures? (Fahad, Oct 31), unseen tasks, failure threshold 50%. No training.
Timely = alarm at or before t_pnr, on timed failures. Venn counts by failure type (results/week3/patterns/failure_types.json) of progress,
gru_phys, safe, hideseek, at each detector's own threshold (their false alarms differ, shown).
OR ensemble of progress and gru_phys: alarm when either alarms. For held-out task t, thresholds come only from the held-out scores of the
successes of the other tasks (per-run max): the same allowed count as the conformal rule, n - ceil((n + 1)(1 - alpha)) runs, is shared by the
pair so that their union stays within it. or_50 shares it equally; or_75 gives progress 3/4; or_25 gives it 1/4. All three are fixed in advance, none
chosen on failures. Each score comes from a model that did not see its own task but did see t, a small difference from 06's thresholds, so no retraining is needed.

python scripts/37_complementarity.py --out results/week3/complementarity
"""

import argparse
import glob
import itertools
import json
import os

import numpy as np

p = argparse.ArgumentParser()
p.add_argument("--scores", default="data/week3_reg/thr50/unseen")
p.add_argument("--baselines", default="results/week3/baselines/unseen/per_episode.json")
p.add_argument("--types", default="results/week3/patterns/failure_types.json")
p.add_argument("--out", default="results/week3/complementarity")
args = p.parse_args()
KEYS = {"fixed 0.05": 0.05, "fixed 0.025": 0.025}
TYPES = ["missed_grasp", "stuck", "drop", "none"]
NAMES = ["progress", "gru_phys", "safe", "hideseek"]
scored = [r for f in sorted(glob.glob(os.path.join(args.scores, "g*", "all_scores.json"))) for r in json.load(open(f)) if r["model"] in NAMES[:2]]
base = [r for r in json.load(open(args.baselines)) if r["model"] in NAMES[2:]]
assert len(glob.glob(os.path.join(args.scores, "g*", "all_scores.json"))) == 10
rows = {m: {r["eid"]: r for r in scored + base if r["model"] == m} for m in NAMES}
kind = json.load(open(args.types))
strip = lambda r: {k: v for k, v in r.items() if k not in ("labels", "scores", "steps", "risk", "ttp")}  # noqa: E731
out = [strip(r) for m in NAMES for r in rows[m].values()]


def thresholds(P, G, alpha, w):
    """Largest shared budget whose union on the calibration runs stays within the allowed count."""
    n = len(P)
    k = int(np.ceil((n + 1) * (1 - alpha)))
    allowed = max(n - k, 0)
    sp, sg = np.sort(P), np.sort(G)
    at = lambda s, c: s[n - c - 1] if c < n else -np.inf  # noqa: E731  c runs above this value
    for total in range(2 * allowed, -1, -1):
        ap = int(round(w * total))
        tp, tg = at(sp, ap), at(sg, total - ap)
        if ((P > tp) | (G > tg)).sum() <= allowed:
            return tp, tg


def first(r, thr):
    above = np.nonzero(np.array(r["scores"]) > thr)[0]
    return r["steps"][above[0]] if len(above) else None


succ = {t: [e for e, r in rows["progress"].items() if r["success"] and r["task"] != t] for t in range(10)}
for w in (0.25, 0.5, 0.75):
    thr = {}
    for t in range(10):
        P = np.array([max(rows["progress"][e]["scores"]) for e in succ[t]])
        G = np.array([max(rows["gru_phys"][e]["scores"]) for e in succ[t]])
        thr[t] = {key: thresholds(P, G, a, w) for key, a in KEYS.items()}
    for eid, rp in rows["progress"].items():
        alarms = {}
        for key in KEYS:
            hits = [x for x in (first(rp, thr[rp["task"]][key][0]), first(rows["gru_phys"][eid], thr[rp["task"]][key][1])) if x is not None]
            alarms[key] = min(hits) if hits else None
        out.append(dict(strip(rp), model=f"or_{int(w * 100)}", alarms=alarms, t_alarm=alarms["fixed 0.05"]))
os.makedirs(args.out, exist_ok=True)
json.dump(out, open(os.path.join(args.out, "per_episode.json"), "w"))

timed = sorted(e for e, r in rows["progress"].items() if not r["success"] and r["t_pnr"] not in (None, 0))
lines = ["# Which timed failures does each detector catch in time?", "", "Unseen tasks, failure threshold 50%, 81 timed failures, natural + perturbed pooled. "
         "Each row counts the failures caught in time by exactly that set of detectors. A detector's false alarm rate is its own.", ""]
for key in KEYS:
    caught = {m: {e for e in timed if rows[m][e]["alarms"][key] is not None and rows[m][e]["alarms"][key] <= rows[m][e]["t_pnr"]} for m in NAMES}
    fa = {m: np.mean([r["alarms"][key] is not None for r in rows[m].values() if r["success"]]) for m in NAMES}
    lines += [f"## {key}", "", "Detector totals: " + ", ".join(f"{m} {len(caught[m])} (false alarms {fa[m]:.3f})" for m in NAMES)
              + f"; caught by at least one: {len(set().union(*caught.values()))} of {len(timed)}.", "",
              "| caught by exactly | all | " + " | ".join(TYPES) + " |", "|---|---|---|---|---|---|"]
    for n in range(4, -1, -1):
        for combo in itertools.combinations(NAMES, n):
            es = [e for e in timed if {m for m in NAMES if e in caught[m]} == set(combo)]
            lines.append(f"| {' + '.join(combo) or 'none'} | {len(es)} | " + " | ".join(str(sum(kind[e] == t for e in es)) for t in TYPES) + " |")
    lines.append("")
open(os.path.join(args.out, "venn.md"), "w").write("\n".join(lines) + "\n")
print("\n".join(lines))
