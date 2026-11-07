"""OR combination progress OR gru_phys_ttp (Fahad, Nov 6, results/plan_nov06.md item 4). Inside each leave-one-task-out fold both thresholds
come from the training-task successes only: the cross-fitted calibration scores saved by 06 --save_calib. One common conformal level a for both
parts, the largest a (grid of 400 steps from the budget down to 0) at which the union false-alarm rate on those calibration successes is at
most the budget. Alarm = first query where either score is above its threshold. Writes OUT/per_episode.json with progress, gru_phys_ttp (their
own fixed thresholds from the same runs) and or_progress_ttp, for 13_report.py and 46_paired_alarms.py, plus OUT/levels.json.

python scripts/47_combo.py --root data/combo/oft/thr50 --out data/combo/oft/thr50/merged
"""

import argparse
import json
import os

import numpy as np

p = argparse.ArgumentParser()
p.add_argument("--root", required=True)
p.add_argument("--groups", type=int, default=10)
p.add_argument("--budgets", nargs="+", type=float, default=[0.05, 0.025])
p.add_argument("--out", required=True)
p.add_argument("--progress_root", default=None, help="dir with progress/g*/ (default ROOT); progress has no seed, so seeds 1 to 4 reuse seed 0")
args = p.parse_args()


def conformal_threshold(run_maxes, alpha):  # same as 06_train_predictor.py
    n = len(run_maxes)
    k = int(np.ceil((n + 1) * (1 - alpha)))
    return np.inf if k > n else float(np.sort(run_maxes)[k - 1])


def first_alarm(r, thr):
    above = np.nonzero(np.asarray(r["scores"], float) > thr)[0]
    return r["steps"][above[0]] if len(above) else None


out, levels = [], {}
for g in range(args.groups):
    rows, cal = {}, {}
    for m in ("progress", "gru_phys_ttp"):
        d = os.path.join(args.progress_root or args.root if m == "progress" else args.root, m, f"g{g}")
        rows[m] = {r["eid"]: r for r in json.load(open(os.path.join(d, "all_scores.json")))}
        cal[m] = {x[0]: x[1] for x in json.load(open(os.path.join(d, "calib.json")))[m]}  # [eid, run max(, per-step scores)]
    ids = sorted(cal["progress"])
    assert ids == sorted(cal["gru_phys_ttp"]), f"group {g}: calibration sets differ"
    cp, cg = np.array([cal["progress"][e] for e in ids]), np.array([cal["gru_phys_ttp"][e] for e in ids])
    for m in rows:
        out += [{k: v for k, v in r.items() if k not in ("labels", "scores", "steps", "risk", "ttp")} for r in rows[m].values()]
    alarms = {e: {} for e in rows["progress"]}
    for b in args.budgets:
        key = f"fixed {b:.2f}" if round(b, 2) == b else f"fixed {b:.3f}"
        for a in np.linspace(b, 0, 401):
            tp, tg = conformal_threshold(cp, a), conformal_threshold(cg, a)
            union = np.mean((cp > tp) | (cg > tg))
            if union <= b:
                break
        levels[f"g{g} {key}"] = dict(level=float(a), union_calib=float(union), n_calib=len(ids), t_progress=tp, t_ttp=tg)
        for e, r in rows["progress"].items():
            hits = [x for x in (first_alarm(r, tp), first_alarm(rows["gru_phys_ttp"][e], tg)) if x is not None]
            alarms[e][key] = min(hits) if hits else None
    for e, r in rows["progress"].items():
        base = {k: v for k, v in r.items() if k not in ("labels", "scores", "steps", "risk", "ttp")}
        out.append(dict(base, model="or_progress_ttp", alarms=alarms[e], t_alarm=alarms[e].get("fixed 0.05")))
os.makedirs(args.out, exist_ok=True)
json.dump(out, open(os.path.join(args.out, "per_episode.json"), "w"), indent=0)
json.dump(levels, open(os.path.join(args.out, "levels.json"), "w"), indent=1)
print(json.dumps(levels, indent=1))
