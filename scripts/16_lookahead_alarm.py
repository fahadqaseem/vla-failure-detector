"""Phase B alarms from the look-ahead futures (Fahad, Oct 23). UPPER BOUND, NOT A DETECTOR (simulator at test time).

Per checkpoint (every 16 steps) of each episode in --la (15_lookahead.py) and --risk (06 --lookahead_out):
  lookahead_nomove   fraction of the 4 futures where the eef moved less than 1 cm
  lookahead_mlp      mean mlp risk at the last query of the futures (mlp that did not see the episode's task)
  lookahead_nosucc   1 if no future succeeded, else 0
Alarm = first checkpoint whose signal is above the threshold. Threshold, leave-one-task-out: conformal 5% (--alpha)
on the per-run max signal of the look-ahead successes of the other tasks. Output per_episode.json in the format of
06_train_predictor.py (key "fixed 0.05"), plus the progress rows of --pred for the same episodes (their own threshold),
so 13_report.py can compare them.

python scripts/16_lookahead_alarm.py --la data/week2_lookahead --risk data/week2_lookahead_mlp --out results/week2/B_lookahead
"""

import argparse
import glob
import json
import os

import numpy as np

p = argparse.ArgumentParser()
p.add_argument("--la", default="data/week2_lookahead")
p.add_argument("--risk", default="data/week2_lookahead_mlp")
p.add_argument("--pred", default="results/predictor_with_perturbed", help="labels and progress rows")
p.add_argument("--alpha", type=float, default=0.05)
p.add_argument("--out", default="results/week2/B_lookahead")
args = p.parse_args()

rows = {r["eid"]: r for r in json.load(open(os.path.join(args.pred, "per_episode.json"))) if r["model"] == "progress"}
eps = []
for f in sorted(glob.glob(os.path.join(args.la, "*.npz"))):
    eid = os.path.splitext(os.path.basename(f))[0]
    la, rk = np.load(f), os.path.join(args.risk, eid + ".npz")
    sig = {"lookahead_nomove": la["no_move"].mean(1), "lookahead_nosucc": (~la["success"].any(1)).astype(float)}
    if os.path.exists(rk):
        sig["lookahead_mlp"] = np.load(rk)["mlp_risk"].mean(1)
    eps.append(dict(row=rows[eid], steps=la["steps"], sig=sig))
print(f"{len(eps)} episodes ({sum(e['row']['success'] for e in eps)} successes)")


def conformal_threshold(run_maxes, alpha):
    n = len(run_maxes)
    k = int(np.ceil((n + 1) * (1 - alpha)))
    return np.inf if k > n else float(np.sort(run_maxes)[k - 1])


key = f"fixed {args.alpha:.2f}"
out = [dict(rows[e["row"]["eid"]]) for e in eps]  # progress rows of the same episodes
lines = [f"# Look-ahead signals (UPPER BOUND: uses the simulator at test time), threshold {key}", ""]
for name in ["lookahead_nomove", "lookahead_mlp", "lookahead_nosucc"]:
    have = [e for e in eps if name in e["sig"]]
    if not have:
        continue
    for t in sorted({e["row"]["task"] for e in have}):
        calib = [e["sig"][name].max() for e in have if e["row"]["task"] != t and e["row"]["success"]]
        thr = conformal_threshold(calib, args.alpha)
        for e in have:
            if e["row"]["task"] != t:
                continue
            above = np.nonzero(e["sig"][name] > thr)[0]
            t_alarm = int(e["steps"][above[0]]) if len(above) else None
            r = e["row"]
            out.append(dict(model=name, task=r["task"], eid=r["eid"], source=r.get("source"), success=r["success"],
                            t_pnr=r["t_pnr"], doomed=r["t_pnr"] == 0, t_alarm=t_alarm, alarms={key: t_alarm},
                            threshold=thr))
        lines.append(f"- {name}, held-out task {t}: threshold {thr:.3f} from {len(calib)} successes")
os.makedirs(args.out, exist_ok=True)
json.dump(out, open(os.path.join(args.out, "per_episode.json"), "w"), indent=1)
open(os.path.join(args.out, "thresholds.md"), "w").write("\n".join(lines) + "\n")
print("\n".join(lines))
