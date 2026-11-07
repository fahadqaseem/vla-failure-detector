"""Seed spread (Fahad, Nov 6, results/plan_nov06.md item 2): gru_phys, gru_phys_frac, gru_phys_ttp with seeds 0 to 4, both policies, three
failure rules, unseen and seen tasks. Seed 0 = the runs of results/week3/regression and results/pi05/regression; seeds 1 to 4 =
data/seeds/{policy}/thr{T}/{split}/s{S}/{model} (28_merge_groups.py already run). Per setting: mean and min to max over the 5 seeds of timely
(alarm at or before t_pnr, failures with t_pnr > 0), false alarms on successes, unnecessary alarms on recoverable failures and median window
t_alarm - t_pnr, and how many seeds beat progress (more timely alarms at the same budget; ties counted apart). Progress has no seed.

python scripts/48_seeds.py --out results/seeds
Realistic inputs (Nov 7): python scripts/48_seeds.py --seed0 oft:data/realistic/oft pi05:data/realistic/pi05 --seed0_sub merged --root data/seeds_real \
    --models gru_robotcontact_ttp gru_robot_ttp --thrs 50 80 --splits unseen --name realistic --out results/seeds
"""

import argparse
import json
import os

import numpy as np

p = argparse.ArgumentParser()
p.add_argument("--seed0", nargs="+", default=["oft:data/week3_reg", "pi05:data/pi05_reg"])
p.add_argument("--root", default="data/seeds")
p.add_argument("--out", default="results/seeds")
p.add_argument("--models", nargs="+", default=["gru_phys_ttp", "gru_phys_frac", "gru_phys"])
p.add_argument("--thrs", nargs="+", type=int, default=[50, 70, 80])
p.add_argument("--splits", nargs="+", default=["unseen", "seen"])
p.add_argument("--seed0_sub", default="", help="subdir of the seed 0 run holding per_episode.json (realistic: merged)")
p.add_argument("--name", default="seeds", help="output file prefix")
args = p.parse_args()
NAMES = {"oft": "OpenVLA-OFT", "pi05": "Pi0.5"}
MODELS = args.models


def metrics(rows, key):
    timed = [r for r in rows if not r["success"] and r["t_pnr"] not in (None, 0)]
    succ = [r for r in rows if r["success"]]
    recov = [r for r in rows if not r["success"] and r["t_pnr"] is None]
    win = [r["alarms"][key] - r["t_pnr"] for r in timed if r["alarms"][key] is not None]
    return dict(timely=sum(w <= 0 for w in win), n=len(timed), fa=np.mean([r["alarms"][key] is not None for r in succ]),
                unn=sum(r["alarms"][key] is not None for r in recov), n_rec=len(recov), win=float(np.median(win)) if win else np.nan)


def spread(v, fmt):
    v = np.asarray(v, float)
    return f"{fmt.format(np.nanmean(v))} ({fmt.format(np.nanmin(v))} to {fmt.format(np.nanmax(v))})"


os.makedirs(args.out, exist_ok=True)
for split in args.splits:
    lines = [f"# Seeds 0 to 4, {split} tasks", "", __doc__.split("\n\n")[0].replace("\n", " "), "",
             "| policy | rule | budget | model | timely mean (min to max) | progress timely | seeds beating progress (ties) | false alarms | "
             "unnecessary | window |", "|---|---|---|---|---|---|---|---|---|---|"]
    for pol, root0 in (x.split(":", 1) for x in args.seed0):
        for thr in args.thrs:
            base = json.load(open(os.path.join(root0, f"thr{thr}", split, args.seed0_sub, "per_episode.json")))
            for key in ("fixed 0.025", "fixed 0.05"):
                pr = metrics([r for r in base if r["model"] == "progress"], key)
                for m in MODELS:
                    per = [metrics([r for r in base if r["model"] == m], key)]
                    for s in (1, 2, 3, 4):
                        per.append(metrics(json.load(open(os.path.join(args.root, pol, f"thr{thr}", split, f"s{s}", m, "per_episode.json"))), key))
                    t = [x["timely"] for x in per]
                    lines.append(f"| {NAMES[pol]} | {thr}% | {key[6:]} | {m} | {spread(t, '{:.1f}')} of {per[0]['n']} | {pr['timely']} | "
                                 f"{sum(x > pr['timely'] for x in t)} of 5 ({sum(x == pr['timely'] for x in t)}) | "
                                 f"{spread([x['fa'] for x in per], '{:.3f}')} (progress {pr['fa']:.3f}) | "
                                 f"{spread([x['unn'] for x in per], '{:.1f}')} of {per[0]['n_rec']} (progress {pr['unn']}) | "
                                 f"{spread([x['win'] for x in per], '{:+.0f}')} (progress {pr['win']:+.0f}) |")
    open(os.path.join(args.out, f"{args.name}_{split}.md"), "w").write("\n".join(lines) + "\n")
    print("\n".join(lines))
