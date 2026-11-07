"""OR combination over seeds (Fahad, Nov 7): progress OR gru_phys_ttp for seeds 0 to 4, both policies, three rules, unseen tasks, budgets 2.5%
and 5%, thresholds from the training-task calibration successes of each fold (47_combo.py, same rule as results/combo). Seed 0 =
data/combo/{policy}/thr{T}/merged, seeds 1 to 4 = data/combo_seeds/{policy}/thr{T}/s{S}/merged (gru_phys_ttp retrained with --save_calib;
progress has no seed and is reused). Per setting: mean and min to max over the 5 seeds of timely (alarm at or before t_pnr, failures with
t_pnr > 0), false alarms on successes and unnecessary alarms on recoverable failures, and how many seeds beat progress (more timely; ties apart).

python scripts/49_combo_seeds.py --out results/combo/seeds.md
"""

import argparse
import json
import os

import numpy as np

p = argparse.ArgumentParser()
p.add_argument("--out", default="results/combo/seeds.md")
args = p.parse_args()
NAMES = {"oft": "OpenVLA-OFT", "pi05": "Pi0.5"}


def metrics(rows, key):
    timed = [r for r in rows if not r["success"] and r["t_pnr"] not in (None, 0)]
    succ = [r for r in rows if r["success"]]
    recov = [r for r in rows if not r["success"] and r["t_pnr"] is None]
    return dict(timely=sum(r["alarms"][key] is not None and r["alarms"][key] <= r["t_pnr"] for r in timed), n=len(timed),
                fa=np.mean([r["alarms"][key] is not None for r in succ]), unn=sum(r["alarms"][key] is not None for r in recov), n_rec=len(recov))


def spread(v, fmt):
    return f"{fmt.format(np.mean(v))} ({fmt.format(min(v))} to {fmt.format(max(v))})"


lines = ["# progress OR gru_phys_ttp over seeds 0 to 4, unseen tasks", "", __doc__.split("\n\n")[0].replace("\n", " "), "",
         "| policy | rule | budget | timely OR, mean (min to max) | progress timely | seeds beating progress (ties) | false alarms OR | progress false alarms | "
         "unnecessary OR | progress unnecessary |", "|---|---|---|---|---|---|---|---|---|---|"]
for pol in ("oft", "pi05"):
    for thr in (50, 70, 80):
        dirs = [f"data/combo/{pol}/thr{thr}/merged"] + [f"data/combo_seeds/{pol}/thr{thr}/s{s}/merged" for s in (1, 2, 3, 4)]
        rows = [json.load(open(os.path.join(d, "per_episode.json"))) for d in dirs]
        for key in ("fixed 0.025", "fixed 0.05"):
            pr = metrics([r for r in rows[0] if r["model"] == "progress"], key)
            per = [metrics([r for r in rs if r["model"] == "or_progress_ttp"], key) for rs in rows]
            t = [x["timely"] for x in per]
            lines.append(f"| {NAMES[pol]} | {thr}% | {key[6:]} | {spread(t, '{:.1f}')} of {pr['n']} | {pr['timely']} | "
                         f"{sum(x > pr['timely'] for x in t)} of 5 ({sum(x == pr['timely'] for x in t)}) | {spread([x['fa'] for x in per], '{:.3f}')} | "
                         f"{pr['fa']:.3f} | {spread([x['unn'] for x in per], '{:.1f}')} of {pr['n_rec']} | {pr['unn']} |")
os.makedirs(os.path.dirname(args.out), exist_ok=True)
open(args.out, "w").write("\n".join(lines) + "\n")
print("\n".join(lines))
