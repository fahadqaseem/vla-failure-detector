"""Report for FailureSpot's methods on our data (30_fs_run.py), Fahad Oct 30: per_episode.json for 13_report.py and one table with
our metrics and FailureSpot's (timestamp and trajectory AUROC, its binary_auroc). LOTO is pooled over the 10 held-out tasks; own =
mean over seeds 0 to 2, unseen tasks only (its seen evaluation set gives the thresholds). gru_phys comes from
results/week3/failurespot/gru_phys/unseen.

python scripts/31_fs_report.py --root results/week3/failurespot
"""

import argparse
import glob
import json
import os
import sys

import numpy as np

sys.path.insert(0, "third_party/failurespot/src")
from failurespot.metrics import binary_auroc  # noqa: E402

p = argparse.ArgumentParser()
p.add_argument("--root", default="results/week3/failurespot")
p.add_argument("--progress", default="results/week2/T1all_unseen_conv/per_episode.json")
p.add_argument("--gru", default=None, help="run dir with gru_phys per_episode.json and summary.md, if it has no all_scores.json")
# Nov 6 (Pi0.5, like for like): evaluate on these tasks only; our rows from an all_scores.json; per-task table with the chunk check
p.add_argument("--tasks", nargs="+", type=int, default=None, help="keep only held-out episodes of these tasks (default all)")
p.add_argument("--ours_scores", default=None, help="all_scores.json with progress and our models (replaces --progress and --gru)")
p.add_argument("--ours_models", nargs="+", default=["gru_phys", "gru_phys_ttp"])
p.add_argument("--table", default="table.md")
p.add_argument("--loto_out", default=None, help="dir for the loto per_episode.json (default ROOT/loto)")
p.add_argument("--task_table", default=None, help="policy data dir (data/pi05): add a per-task table with gates and results/<policy>/chunks checks")
args = p.parse_args()
METHODS = [f"{m}_{a}" for m in ("failurespot", "safe", "supervised_random", "actprobe") for a in ("mlp", "lstm")] + ["logpzo"]
KEYS = ["fixed 0.05", "fixed 0.025"]
keep = (lambda eid: True) if args.tasks is None else (lambda eid: int(eid[1:3]) in args.tasks)  # noqa: E731
DROP = ("labels", "scores", "steps", "risk", "ttp")


def ours(rows, key):
    """Our report's columns (same definitions as 13_report.py)."""
    timed = [r for r in rows if not r["success"] and r["t_pnr"] not in (None, 0)]
    succ = [r for r in rows if r["success"]]
    recov = [r for r in rows if not r["success"] and r["t_pnr"] is None]
    window = [r["alarms"][key] - r["t_pnr"] for r in timed if r["alarms"][key] is not None]
    fa = lambda ss: float(np.mean([r["alarms"][key] is not None for r in ss])) if ss else float("nan")  # noqa: E731
    return dict(timely=sum(w <= 0 for w in window), timed=len(timed), fa_nat=fa([r for r in succ if "_p" not in r["eid"]]),
                fa_pert=fa([r for r in succ if "_p" in r["eid"]]),
                unnecessary=sum(r["alarms"][key] is not None for r in recov), recov=len(recov),
                window=float(np.median(window)) if window else float("nan"))


def aurocs(scores, labels, lengths, failed):
    ends = np.cumsum(lengths)[:-1]
    return binary_auroc(labels, scores), binary_auroc(failed, [s.max() for s in np.split(scores, ends)])


def npz_kept(z):
    """Per-query scores and labels of the kept episodes of one 30_fs_run.py npz."""
    ends = np.cumsum(z["lengths"])[:-1]
    sc, lab = np.split(z["scores"], ends), np.split(z["labels"], ends)
    k = [i for i, e in enumerate(z["eids"]) if keep(str(e))]
    return [sc[i] for i in k], [lab[i] for i in k], [str(z["eids"][i]) for i in k]


def na(v):
    """AUROC cell: n/a when it cannot be computed."""
    return "n/a" if v is None or (isinstance(v, (float, np.floating)) and np.isnan(v)) else f"{v:.3f}"


def cells(o):
    f = lambda v, spec: "n/a" if v is None or (isinstance(v, float) and np.isnan(v)) else format(v, spec)  # noqa: E731
    return (f"{f(o['timely'], '.3g')} of {f(o['timed'], '.3g')} | {f(o['fa_nat'], '.3f')} / {f(o['fa_pert'], '.3f')} | "
            f"{f(o['unnecessary'], '.3g')} of {f(o['recov'], '.3g')} | {f(o['window'], '+.0f')}")


lines = ["# FailureSpot methods vs gru_phys on our data", "",
         "Timely of failures with t_pnr > 0; false alarms natural / perturbed successes; unnecessary = alarms on recoverable failures; "
         "window = median t_alarm - t_pnr over alarmed failures (negative = before t_pnr). AUROC: FailureSpot's metrics, labels 1 from "
         "t_pnr on. Natural and perturbed pooled (7 of 10 tasks perturbed, perturbed_v2 tasks 0, 1, 4, 7). own = its split, seeds 0 to 2, "
         "unseen tasks, mean; loto = leave one task out, pooled.", "",
         "| split | model | timestamp AUROC | trajectory AUROC | " + " | ".join(
             f"timely {k[6:]} | false alarms {k[6:]} | unnecessary {k[6:]} | window {k[6:]}" for k in KEYS) + " |",
         "|---|---|---|---|" + "---|---|---|---|" * len(KEYS)]
ours_all = json.load(open(args.ours_scores)) if args.ours_scores else None
src = ours_all if ours_all is not None else json.load(open(args.progress))
loto_rows = [{k: v for k, v in r.items() if k not in DROP} for r in src if r["model"] == "progress" and keep(r["eid"])]
if args.tasks is not None:
    lines[2] += f" Evaluated on held-out episodes of tasks {', '.join(map(str, args.tasks))} only (failures and successes)."
for m in METHODS:
    fs = [os.path.join(args.root, "loto", f"g{g}", m) for g in range(10)]
    have = [f for f in fs if os.path.exists(f + ".json")]
    if len(have) < 10:
        print(f"loto {m}: only {len(have)} of 10 groups", flush=True)
        if not have:
            continue
    rows = [r for f in have for r in json.load(open(f + ".json"))["rows"]["held_out"] if keep(r["eid"])]
    loto_rows += rows
    kept = [npz_kept(np.load(f + ".npz")) for f in have]
    sc, lab, ids = [a for x in kept for a in x[0]], [a for x in kept for a in x[1]], [a for x in kept for a in x[2]]
    failed = {r["eid"]: not r["success"] for r in rows}
    auc = aurocs(np.concatenate(sc), np.concatenate(lab), [len(a) for a in sc], [failed[e] for e in ids]) if sc else (np.nan, np.nan)
    note = "" if len(have) == 10 else f" ({len(have)} of 10 tasks)"
    lines.append(f"| loto | {m}{note} | {na(auc[0])} | {na(auc[1])} | " + " | ".join(cells(ours(rows, k)) for k in KEYS) + " |")
if ours_all is not None:
    for m in args.ours_models:
        rows = [r for r in ours_all if r["model"] == m and keep(r["eid"])]
        auc = aurocs(np.concatenate([r["scores"] for r in rows]), np.concatenate([r["labels"] for r in rows]),
                     [len(r["scores"]) for r in rows], [not r["success"] for r in rows])
        lines.append(f"| loto | {m} (ours) | {na(auc[0])} | {na(auc[1])} | " + " | ".join(cells(ours(rows, k)) for k in KEYS) + " |")
        loto_rows += [{k: v for k, v in r.items() if k not in DROP} for r in rows]
LO = args.loto_out or os.path.join(args.root, "loto")
os.makedirs(LO, exist_ok=True)
json.dump(loto_rows, open(os.path.join(LO, "per_episode.json"), "w"))
gp = os.path.join(args.root, "gru_phys", "unseen", "all_scores.json")
if os.path.exists(gp):
    rows = [r for r in json.load(open(gp)) if r["model"] == "gru_phys"]
    auc = aurocs(np.concatenate([r["scores"] for r in rows]), np.concatenate([r["labels"] for r in rows]),
                 [len(r["scores"]) for r in rows], [not r["success"] for r in rows])
    lines.append(f"| loto | gru_phys (ours) | {na(auc[0])} | {na(auc[1])} | " + " | ".join(cells(ours(rows, k)) for k in KEYS) + " |")
if args.gru and ours_all is None:
    rows = [r for r in json.load(open(os.path.join(args.gru, "per_episode.json"))) if r["model"] == "gru_phys"]
    auc = next(line.split("|")[4].strip() for line in open(os.path.join(args.gru, "summary.md")) if line.startswith("| gru_phys |"))
    lines.append(f"| loto | gru_phys (ours) | {auc} | n/a | " + " | ".join(cells(ours(rows, k)) for k in KEYS) + " |")
for m in METHODS:
    per = []
    for s in range(3):
        f = os.path.join(args.root, "own", f"g{s}", m + ".json")
        if os.path.exists(f):
            x = json.load(open(f))
            x["rows"]["unseen"] = [r for r in x["rows"]["unseen"] if keep(r["eid"])]
            if args.tasks is not None:  # FailureSpot's own AUROCs are over all its unseen tasks: recompute on the kept ones
                failed = {r["eid"]: not r["success"] for r in x["rows"]["unseen"]}
                sc, lab, ids = npz_kept(np.load(f[:-5] + ".npz"))  # the own npz also holds its seen evaluation set
                sel = [i for i, e in enumerate(ids) if e in failed]
                sc, lab, ids = [sc[i] for i in sel], [lab[i] for i in sel], [ids[i] for i in sel]
                x["metrics"]["unseen"] = dict(zip(("timestamp_auroc", "trajectory_auroc"), aurocs(
                    np.concatenate(sc), np.concatenate(lab), [len(a) for a in sc], [failed[e] for e in ids]) if sc else (np.nan, np.nan)))
            per.append(x)
    if not per:
        continue
    means = [{c: float(np.nanmean([ours(x["rows"]["unseen"], k)[c] for x in per])) for c in ("timely", "timed", "fa_nat", "fa_pert", "unnecessary", "recov", "window")}
             for k in KEYS]
    a = [np.mean([x["metrics"]["unseen"][c] for x in per]) for c in ("timestamp_auroc", "trajectory_auroc")]
    note = "" if len(per) == 3 else f" ({len(per)} of 3 seeds)"
    lines.append(f"| own | {m}{note} | {na(a[0])} | {na(a[1])} | " + " | ".join(cells(o) for o in means) + " |")
for s in range(3):
    rows = [r for f in sorted(glob.glob(os.path.join(args.root, "own", f"g{s}", "*.json"))) if not f.endswith("per_episode.json")
            for r in json.load(open(f))["rows"]["unseen"]]
    json.dump(rows, open(os.path.join(args.root, "own", f"g{s}", "per_episode.json"), "w"))
if args.task_table:
    pol = os.path.basename(args.task_table.rstrip("/"))
    lines += ["", "## Per task: replay gate and the 50-step chunk check", "",
              "41_pi_chunks.py replays the recorded actions and asks the policy again with each query's flow seed; difference = max |recovered first 8 "
              "actions - recorded actions| per query (0 = chunk reproduced). Tasks whose natural gate failed (2, 3, 8, 9) may not reproduce.", "",
              "| task | natural gate | held-out episodes (progress rows) | failures with t_pnr > 0 | chunk queries | median difference | max difference |",
              "|---|---|---|---|---|---|---|"]
    for t in range(10):
        gate = "pass" if os.path.exists(f"{args.task_table}/natural/task{t:02d}/GATE_PASS") else "FAIL"
        mine = [r for r in loto_rows if r["model"] == "progress" and int(r["eid"][1:3]) == t]
        cf = f"results/{pol}/chunks/task{t}.json"
        c = json.load(open(cf)) if os.path.exists(cf) else None
        fmt = lambda v: "n/a" if v is None else f"{v:.4f}"  # noqa: E731
        cc = f"{c['queries']} | {fmt(c['median_max_diff'])} | {fmt(c['max_diff'])}" if c else "n/a | n/a | n/a"
        lines.append(f"| {t} | {gate} | {len(mine)} | {sum(not r['success'] and r['t_pnr'] not in (None, 0) for r in mine)} | {cc} |")
open(os.path.join(args.root, args.table), "w").write("\n".join(lines) + "\n")
print("\n".join(lines))
