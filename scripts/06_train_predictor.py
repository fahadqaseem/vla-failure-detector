"""Per-step predictor of the point of no return, evaluated leave-one-task-out (decisions in CLAUDE.md).

Data, one row per policy query (every 8 steps):
  inputs  = features_mean (4096, last-layer hidden states at the action tokens, mean over the 56 tokens)
            + the action chunk it produced (8 x 7) + eef position (3) + gripper qpos (2).
            Never the step index or anything that counts time.
  label   = 1 at and after t_pnr, else 0 (tau 0.5 on the full scan; successes and recoverable failures all 0).
  risk    = 1 - (successful replays / K) at that checkpoint, only for scanned episodes (MSE masked elsewhere).
Episodes used: every scanned episode (data/full_scans/*.json) plus ALL natural successes (label 0).
Unscanned failures have no label and are left out (the SAFE-style baseline uses them, since it only
needs success/fail).

Training weights: every episode has the same total weight (each row gets 1 / rows in its episode), then
positive rows are scaled so that positives and negatives have the same total weight. Both losses use them.

Models (same inputs, standardised with the training rows):
  logreg    one linear layer -> p = sigmoid(logit); loss = BCE(p, label) + MSE(p, risk)
  mlp       linear 256 -> ReLU -> linear 1; same loss
  safe      linear probe like SAFE: label = 1 at every step of a failed episode; BCE only
  timer     score = policy step (no training): shows how far counting steps gets
  progress  steps-since-progress (RESCUE): chunk boundaries since the eef last moved more than 0.01 m
            between successive boundaries (no training)

Leave-one-task-out: for each task, train on the other 9 and test on it.
Conformal threshold from ALL successes of the 9 training tasks. Their scores must come from a model that
did not see their task (as at test time), so they are cross-fitted: for each training task u, a model
trained on the other 8 tasks scores u's successes. Threshold = the ceil((n+1)(1-alpha))-th smallest
per-run max score over the n calibration runs. Alarm = first query step whose score is above it.
False alarms are measured on ALL successes of the held-out task.

Metrics (pooled over the 10 held-out tasks):
  AUROC per step over the whole run (sklearn); false-alarm rate on held-out successes;
  on labelled failures with t_pnr > 0 (doomed-from-start episodes, t_pnr = 0, are left out of timing):
  recall (any alarm), timely (alarm at or before t_pnr, RESCUE-style), late (after), missed,
  lead time = t_pnr - t_alarm (positive = early), mean |t_alarm - t_pnr|, median eta = t_alarm / t_pnr.

python scripts/06_train_predictor.py --scans "data/full_scans/*.json" --episodes "data/natural/*/*.npz" --out results/predictor
"""

import argparse
import glob
import json
import os

import numpy as np
import torch
from sklearn.metrics import roc_auc_score

p = argparse.ArgumentParser()
p.add_argument("--scans", default="data/full_scans/*.json")
p.add_argument("--episodes", default="data/natural/*/*.npz")
p.add_argument("--tau_min_success", type=int, default=3, help="recoverable if >= this many of K=4 replays succeed (tau 0.5)")
p.add_argument("--alpha", type=float, default=0.05, help="target false-alarm rate on successful runs")
p.add_argument("--progress_m", type=float, default=0.01, help="eef move (m) between boundaries that counts as progress")
p.add_argument("--epochs", type=int, default=300)
p.add_argument("--lr", type=float, default=1e-3)
p.add_argument("--weight_decay", type=float, default=1e-3)
p.add_argument("--hidden", type=int, default=256)
p.add_argument("--seed", type=int, default=0)
p.add_argument("--out", default="results/predictor")
args = p.parse_args()


def t_pnr_from_scan(scan):
    """First checkpoint from which every later checkpoint is not recoverable (None if the last one is)."""
    assert scan["params"]["K"] == 4, "tau_min_success assumes K = 4"
    ok = [sum(s) >= args.tau_min_success for s in scan["successes"]]
    if ok[-1]:
        return None
    i = len(ok) - 1
    while i > 0 and not ok[i - 1]:
        i -= 1
    return scan["checkpoints"][i]


def steps_since_progress(eef_at_queries):
    """Chunk boundaries since the eef last moved more than progress_m between successive boundaries."""
    out, count = [0], 0
    for k in range(1, len(eef_at_queries)):
        moved = np.linalg.norm(eef_at_queries[k] - eef_at_queries[k - 1]) > args.progress_m
        count = 0 if moved else count + 1
        out.append(count)
    return np.array(out, np.float32)


# ---- load episodes ----
scans = {}
for f in glob.glob(args.scans):
    s = json.load(open(f))
    scans[s["episode_id"]] = s

episodes = []  # one dict per episode
for f in sorted(glob.glob(args.episodes)):
    ep = np.load(f, allow_pickle=True)
    if bool(ep["induced"]):
        continue
    eid = os.path.splitext(os.path.basename(f))[0]
    success, scan = bool(ep["success"]), scans.get(eid)
    q = ep["query_steps"].astype(int)
    actions = ep["actions"]
    chunks = np.stack([actions[s:s + 8].reshape(-1) if s + 8 <= len(actions)
                       else np.pad(actions[s:], ((0, s + 8 - len(actions)), (0, 0))).reshape(-1) for s in q])
    x = np.concatenate([ep["features_mean"], chunks, ep["eef"][q], ep["query_grippers"]], axis=1).astype(np.float32)
    t_pnr = t_pnr_from_scan(scan) if scan else None
    label = np.zeros(len(q), np.float32) if t_pnr is None else (q >= t_pnr).astype(np.float32)
    risk = np.full(len(q), np.nan, np.float32)
    if scan:
        by_step = {c: 1 - sum(s) / len(s) for c, s in zip(scan["checkpoints"], scan["successes"])}
        risk = np.array([by_step.get(int(s), np.nan) for s in q], np.float32)
    episodes.append(dict(eid=eid, task=int(ep["task_id"]), success=success, scanned=scan is not None,
                         t_pnr=t_pnr, doomed=t_pnr == 0, steps=q, x=x, label=label, risk=risk,
                         progress=steps_since_progress(ep["eef"][q])))

labelled = [e for e in episodes if e["scanned"] or e["success"]]
n_fail_lab = sum(not e["success"] and e["scanned"] for e in episodes)
print(f"{len(episodes)} natural episodes; labelled: {len(labelled)} "
      f"({n_fail_lab} scanned failures, {sum(e['success'] for e in labelled)} successes, "
      f"{sum(e['doomed'] for e in episodes)} doomed from start)")


# ---- models ----
def train(rows, model_name):
    """rows: list of episodes. Returns a function: episode -> per-step score."""
    torch.manual_seed(args.seed)
    X = np.concatenate([e["x"] for e in rows])
    mu, sd = X.mean(0), X.std(0) + 1e-6
    X = torch.tensor((X - mu) / sd)
    if model_name == "safe":
        y = np.concatenate([np.full(len(e["steps"]), float(not e["success"]), np.float32) for e in rows])
        r = np.full_like(y, np.nan)
    else:
        y = np.concatenate([e["label"] for e in rows])
        r = np.concatenate([e["risk"] for e in rows])
    # Each episode weighs the same; then positives and negatives get the same total weight.
    w = np.concatenate([np.full(len(e["steps"]), 1 / len(e["steps"]), np.float32) for e in rows])
    w[y == 1] *= w[y == 0].sum() / max(w[y == 1].sum(), 1e-12)
    w = torch.tensor(w / w.sum())
    y, r = torch.tensor(y), torch.tensor(r)
    has_risk = ~torch.isnan(r)
    d = X.shape[1]
    net = (torch.nn.Sequential(torch.nn.Linear(d, args.hidden), torch.nn.ReLU(), torch.nn.Linear(args.hidden, 1))
           if model_name == "mlp" else torch.nn.Linear(d, 1))
    opt = torch.optim.Adam(net.parameters(), lr=args.lr, weight_decay=args.weight_decay)
    for _ in range(args.epochs):  # full batch
        logit = net(X).squeeze(1)
        loss = (w * torch.nn.functional.binary_cross_entropy_with_logits(logit, y, reduction="none")).sum()
        if has_risk.any():
            wr = w[has_risk] / w[has_risk].sum()
            loss = loss + (wr * (torch.sigmoid(logit[has_risk]) - r[has_risk]) ** 2).sum()
        opt.zero_grad()
        loss.backward()
        opt.step()
    net.eval()

    def score(e):
        with torch.no_grad():
            return torch.sigmoid(net(torch.tensor((e["x"] - mu) / sd)).squeeze(1)).numpy()
    return score


def fit(model_name, train_eps):
    """Train on these episodes (or nothing, for the rule-based baselines)."""
    if model_name == "timer":
        return lambda e: e["steps"].astype(np.float32)
    if model_name == "progress":
        return lambda e: e["progress"]
    if model_name == "safe":
        return train(train_eps, "safe")
    return train([e for e in train_eps if e["scanned"] or e["success"]], model_name)


def conformal_threshold(run_maxes):
    n = len(run_maxes)
    k = int(np.ceil((n + 1) * (1 - args.alpha)))
    return np.inf if k > n else float(np.sort(run_maxes)[k - 1])


def first_alarm(e, s, thr):
    above = np.nonzero(s > thr)[0]
    return int(e["steps"][above[0]]) if len(above) else None


# ---- leave-one-task-out ----
models = ["timer", "progress", "safe", "logreg", "mlp"]
rows_out = []  # one row per (model, held-out episode)
tasks = sorted({e["task"] for e in episodes})
for test_task in tasks:
    train_tasks = [t for t in tasks if t != test_task]
    train_eps = [e for e in episodes if e["task"] != test_task]
    test = [e for e in labelled if e["task"] == test_task]
    for m in models:
        # Calibration scores for each training task's successes, from a model that did not see that task.
        calib_maxes = []
        for u in train_tasks:
            score_u = fit(m, [e for e in train_eps if e["task"] != u])
            calib_maxes += [score_u(e).max() for e in train_eps if e["task"] == u and e["success"]]
        thr = conformal_threshold(calib_maxes)
        score = fit(m, train_eps)
        for e in test:
            s = score(e)
            rows_out.append(dict(model=m, task=test_task, eid=e["eid"], success=e["success"], t_pnr=e["t_pnr"],
                                 doomed=e["doomed"], t_alarm=first_alarm(e, s, thr), threshold=thr,
                                 labels=e["label"].tolist(), scores=s.tolist()))
    print(f"held-out task {test_task}: {len(train_eps)} training episodes, {len(test)} test episodes", flush=True)


# ---- metrics ----
def summarise(rows):
    labels = np.concatenate([r["labels"] for r in rows])
    scores = np.concatenate([r["scores"] for r in rows])
    auroc = roc_auc_score(labels, scores) if 0 < labels.sum() < len(labels) else float("nan")
    succ = [r for r in rows if r["success"]]
    timed = [r for r in rows if not r["success"] and r["t_pnr"] not in (None, 0)]
    recov = [r for r in rows if not r["success"] and r["t_pnr"] is None]
    alarmed = [r for r in timed if r["t_alarm"] is not None]
    lead = [r["t_pnr"] - r["t_alarm"] for r in alarmed]
    return dict(
        auroc=auroc,
        false_alarm=np.mean([r["t_alarm"] is not None for r in succ]) if succ else float("nan"),
        n_success=len(succ), n_timed=len(timed), n_recoverable_fail=len(recov),
        alarms_on_recoverable_fail=sum(r["t_alarm"] is not None for r in recov),
        recall=len(alarmed) / len(timed) if timed else float("nan"),
        timely=sum(x >= 0 for x in lead), late=sum(x < 0 for x in lead), missed=len(timed) - len(alarmed),
        median_lead=np.median(lead) if lead else float("nan"),
        mean_abs_err=np.mean(np.abs(lead)) if lead else float("nan"),
        median_eta=np.median([r["t_alarm"] / r["t_pnr"] for r in alarmed]) if alarmed else float("nan"),
    )


os.makedirs(args.out, exist_ok=True)
lines = ["# Per-step t_pnr predictor, leave-one-task-out", "",
         f"Labels: full replay scans, K 4, tau 0.5 (>= {args.tau_min_success} of 4 succeed = recoverable). "
         f"Scanned failures: {n_fail_lab}; doomed from start (t_pnr 0, left out of timing): "
         f"{sum(e['doomed'] for e in episodes)}. Training and test use all natural successes. "
         f"Threshold: conformal, alpha {args.alpha}, from cross-fitted scores of all training-task successes. "
         f"epochs {args.epochs}, lr {args.lr}, weight decay {args.weight_decay}, hidden {args.hidden}, seed {args.seed}, "
         f"progress {args.progress_m} m.",
         "", "Timely = alarm at or before t_pnr; late = after; lead = t_pnr - t_alarm (positive = early); "
         "|err| = mean |t_alarm - t_pnr|; all over alarmed failures with t_pnr > 0.", "",
         "| model | per-step AUROC | false alarms on successes | failures with t_pnr > 0 | recall | timely | late | missed | median lead (steps) | mean abs err (steps) | median eta | alarms on recoverable failures |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|"]
for m in models:
    s = summarise([r for r in rows_out if r["model"] == m])
    lines.append(f"| {m} | {s['auroc']:.3f} | {s['false_alarm']:.3f} (of {s['n_success']}) | {s['n_timed']} | {s['recall']:.2f} | "
                 f"{s['timely']} | {s['late']} | {s['missed']} | {s['median_lead']:.1f} | {s['mean_abs_err']:.1f} | "
                 f"{s['median_eta']:.2f} | {s['alarms_on_recoverable_fail']} of {s['n_recoverable_fail']} |")
lines += ["", "Labelled failures, per model: t_pnr -> t_alarm (lead time)", ""]
for r in rows_out:
    if not r["success"]:
        flag = " (doomed from start)" if r["doomed"] else ""
        lead = (r["t_pnr"] - r["t_alarm"]) if r["t_alarm"] is not None and r["t_pnr"] is not None else None
        lines.append(f"- {r['model']} {r['eid']}: t_pnr {r['t_pnr']}{flag} -> t_alarm {r['t_alarm']} "
                     f"(lead {lead}, threshold {r['threshold']:.3f})")
text = "\n".join(lines) + "\n"
open(os.path.join(args.out, "summary.md"), "w").write(text)
with open(os.path.join(args.out, "per_episode.json"), "w") as f:
    json.dump([{k: v for k, v in r.items() if k not in ("labels", "scores")} for r in rows_out], f, indent=1)
print(text)
