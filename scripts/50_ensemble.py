"""Seed ensemble of gru_phys_ttp (Fahad, Nov 7, plan item (a)): per-step score = mean over seeds 0 to 4. In each leave-one-task-out fold the
thresholds are fixed conformal on the cross-fitted training-task successes, using the seed mean of their per-step calibration scores (06
--save_calib). or_progress_ens = progress OR the ensemble with the common-level rule of 47_combo.py (progress calibration from data/combo).
Writes OUT/all_scores.json (gru_phys_ttp_ens, with scores) and OUT/per_episode.json (gru_phys_ttp_ens and or_progress_ens).

python scripts/50_ensemble.py --root data/ens/oft/thr70 --combo data/combo/oft/thr70 --out data/ens/oft/thr70/merged
"""

import argparse
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from audit_lib import DROP, conformal_threshold, first_alarm  # noqa: E402

p = argparse.ArgumentParser()
p.add_argument("--root", required=True, help="dir with s0 .. s4 / g0 .. g9 runs of gru_phys_ttp (--save_calib)")
p.add_argument("--combo", required=True, help="dir with progress/g*/calib.json and all_scores.json")
p.add_argument("--seeds", type=int, default=5)
p.add_argument("--groups", type=int, default=10)
p.add_argument("--alphas", nargs="+", type=float, default=[0.025, 0.05, 0.10, 0.20])
p.add_argument("--out", required=True)
args = p.parse_args()
key = lambda a: f"fixed {a:.2f}" if round(a, 2) == a else f"fixed {a:.3f}"  # noqa: E731

ens_rows, per = [], []
for g in range(args.groups):
    runs = [os.path.join(args.root, f"s{s}", f"g{g}") for s in range(args.seeds)]
    if not all(os.path.exists(os.path.join(d, "all_scores.json")) for d in runs):  # fresh test: held-out task with no new episodes
        print(f"group {g}: no scores, left out")
        continue
    test = [{r["eid"]: r for r in json.load(open(os.path.join(d, "all_scores.json")))} for d in runs]
    cal = [{x[0]: np.array(x[2]) for x in json.load(open(os.path.join(d, "calib.json")))["gru_phys_ttp"]} for d in runs]
    ids = sorted(cal[0])
    assert all(sorted(c) == ids for c in cal), f"group {g}: calibration sets differ between seeds"
    cal_max = np.array([np.mean([c[e] for c in cal], axis=0).max() for e in ids])
    pc = {x[0]: x[1] for x in json.load(open(os.path.join(args.combo, "progress", f"g{g}", "calib.json")))["progress"]}
    pc_max = np.array([pc[e] for e in ids])
    prog = {r["eid"]: r for r in json.load(open(os.path.join(args.combo, "progress", f"g{g}", "all_scores.json")))}
    thr = {key(a): conformal_threshold(cal_max, a) for a in args.alphas}
    # OR with progress: largest common conformal level whose union false-alarm rate on the calibration successes stays within the budget
    orth = {}
    for a in args.alphas:
        for lv in np.linspace(a, 0, 401):
            tp, tg = conformal_threshold(pc_max, lv), conformal_threshold(cal_max, lv)
            if np.mean((pc_max > tp) | (cal_max > tg)) <= a:
                break
        orth[key(a)] = (tp, tg)
    for e, r0 in test[0].items():
        s = np.mean([t[e]["scores"] for t in test], axis=0)
        r = dict(r0, model="gru_phys_ttp_ens", scores=s.tolist())
        r["alarms"] = {k: first_alarm(r, t) for k, t in thr.items()}
        r["t_alarm"] = r["alarms"].get("fixed 0.05")
        ens_rows.append(r)
        per.append({k: v for k, v in r.items() if k not in DROP})
        o = {k: min([x for x in (first_alarm(prog[e], tp), first_alarm(r, tg)) if x is not None], default=None) for k, (tp, tg) in orth.items()}
        per.append(dict({k: v for k, v in r.items() if k not in DROP}, model="or_progress_ens", alarms=o, t_alarm=o.get("fixed 0.05")))
os.makedirs(args.out, exist_ok=True)
json.dump(ens_rows, open(os.path.join(args.out, "all_scores.json"), "w"))
json.dump(per, open(os.path.join(args.out, "per_episode.json"), "w"), indent=0)
print(f"{args.out}: {len(ens_rows)} episodes")
