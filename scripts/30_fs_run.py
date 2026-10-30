"""FailureSpot's methods on our data, using its code unchanged (third_party/failurespot), Fahad Oct 30.
--mode own: its split (3 seen tasks, 60% train, seeds 0 to 2, seen_task_splits of its config), budget 15% of the seen trajectories.
  Fixed thresholds from the successes of its seen evaluation set, as its own conformal band.
--mode loto: leave one task out (--group = held-out task). Budget 15% of the training trajectories. Thresholds as in
  06_train_predictor.py (conformal quantile of the per-run max over training-group successes scored by a model that did not see
  their task), except the cross-fit uses 3 inner task folds, not one per task, to stay affordable.
validate_trajectories is skipped (it assumes 50 runs per task). Labels: 1 from t_pnr on, doomed all 1, recoverable and successes 0.
Each method writes OUT/<method>.npz (eids, per-query scores) and OUT/<method>.json (rows for 13_report.py).
"""

import argparse
import json
import os
import sys
import time

import numpy as np
import torch

sys.path.insert(0, "third_party/failurespot/src")
from failurespot.config import ExperimentConfig  # noqa: E402
from failurespot.data import DataSplit, Trajectory, split_trajectories  # noqa: E402
from failurespot.experiment import fit_trainable_method  # noqa: E402
from failurespot.logpzo import fit_logpzo, score_logpzo  # noqa: E402
from failurespot.metrics import evaluate_scores  # noqa: E402
from failurespot.models import build_detector  # noqa: E402
from failurespot.signals import action_probe_features  # noqa: E402
from failurespot.training import predict_scores, repeated_trajectory_labels, seed_everything, train_detector  # noqa: E402

p = argparse.ArgumentParser()
p.add_argument("--mode", choices=["own", "loto"], required=True)
p.add_argument("--group", type=int, required=True, help="own: seed; loto: held-out task")
p.add_argument("--methods", nargs="+", required=True, help="e.g. failurespot_mlp safe_lstm logpzo")
p.add_argument("--data", default="data/failurespot/trajectories.npz")
p.add_argument("--device", default="cpu")
p.add_argument("--out", required=True)
args = p.parse_args()

KEYS = {"fixed 0.025": 0.025, "fixed 0.05": 0.05}
d = np.load(args.data)
off, eids = d["offsets"], d["eids"].tolist()
meta = {}
trajectories = []
features, actions = d["features"], d["actions"]
for i, eid in enumerate(eids):
    a, b = off[i], off[i + 1]
    steps = np.arange(b - a) * 8  # query_steps start at 0 and advance by the chunk
    t_pnr = int(d["t_pnr"][i])
    labels = np.zeros(b - a, np.float32) if t_pnr < 0 else (steps >= t_pnr).astype(np.float32)
    success = bool(d["success"][i])
    meta[f"oft:task{int(d['task'][i])}:episode{i}"] = dict(
        eid=eid, task=int(d["task"][i]), source=str(d["source"][i]), success=success, steps=steps,
        t_pnr=None if t_pnr < 0 else t_pnr, doomed=t_pnr == 0)
    trajectories.append(Trajectory("oft", int(d["task"][i]), i, features[a:b], actions[a:b, None], labels, int(not success)))
del features, actions
config = ExperimentConfig.load("third_party/failurespot/configs/openvla.yaml")
config.policy.name = "oft"
config.training.device = args.device
config.data.seen_task_count = 1  # budget = annotation_fraction x trajectories_per_task, set per fit below
os.makedirs(args.out, exist_ok=True)


def fit_score(method, train, test, seed):
    """Train one method; returns {key: per-query scores} for test."""
    config.training.seed = seed
    empty = DataSplit(train, [], [], [], [])
    name, _, arch = method.rpartition("_")
    if method == "logpzo":
        return score_logpzo(fit_logpzo(train, config).model, test, args.device)
    if name == "actprobe":
        seed_everything(seed)
        tf = lambda items: [t.with_features(action_probe_features(t, 1, config.signals.ema_beta)) for t in items]  # noqa: E731
        probe = tf(train)
        model = build_detector(6, config.model, arch)
        train_detector(model, probe, repeated_trajectory_labels(probe), config, arch, config.training.baseline_epochs)
        return predict_scores(model, tf(test), args.device)
    model, _, _ = fit_trainable_method(name, arch, empty, config, ckpt)
    return predict_scores(model, test, args.device)


def threshold(calib, alpha):
    """Same rule as 06_train_predictor.py conformal_threshold."""
    k = int(np.ceil((len(calib) + 1) * (1 - alpha)))
    return np.inf if k > len(calib) else float(np.sort(calib)[k - 1])


def rows_for(model, test, scores, thr):
    out = []
    for t in test:
        m = meta[t.key]
        alarms = {}
        for key, v in thr.items():
            above = np.nonzero(scores[t.key] > v)[0]
            alarms[key] = int(m["steps"][above[0]]) if len(above) else None
        out.append(dict(model=model, task=m["task"], eid=m["eid"], source=m["source"], success=m["success"], t_pnr=m["t_pnr"],
                        doomed=m["doomed"], t_alarm=alarms["fixed 0.05"], alarms=alarms))
    return out


for method in args.methods:
    done = os.path.join(args.out, method + ".json")
    if os.path.exists(done):  # a preempted array task restarts here
        continue
    t0 = time.time()
    ckpt = __import__("pathlib").Path(f"data/failurespot/ckpt/{args.mode}_{args.group}_{method}")
    seed = args.group if args.mode == "own" else 0
    if args.mode == "own":
        seen = config.data.seen_task_splits[seed % 3]
        split = split_trajectories(trajectories, seen, 0.60, seed)
        config.data.trajectories_per_task = len(split.train) + len(split.seen_evaluation)
        test = split.seen_evaluation + split.unseen_evaluation
        scores = fit_score(method, split.train, test, seed)
        calib = [scores[t.key].max() for t in split.seen_evaluation if t.trajectory_label == 0]
        groups = {"seen": split.seen_evaluation, "unseen": split.unseen_evaluation}
    else:
        train = [t for t in trajectories if t.task_id != args.group]
        test = [t for t in trajectories if t.task_id == args.group]
        tasks = sorted({t.task_id for t in train})
        calib = []
        for fold in range(3):
            out = set(tasks[fold::3])
            inner = [t for t in train if t.task_id not in out]
            held = [t for t in train if t.task_id in out and t.trajectory_label == 0]
            config.data.trajectories_per_task = len(inner)
            inner_scores = fit_score(method, inner, held, seed)
            calib += [inner_scores[t.key].max() for t in held]
            print(f"{method} inner fold {fold}: {time.time() - t0:.0f} s", flush=True)
        config.data.trajectories_per_task = len(train)
        scores = fit_score(method, train, test, seed)
        groups = {"held_out": test}
    thr = {k: threshold(calib, a) for k, a in KEYS.items()}
    metrics = {g: evaluate_scores(ts, scores) for g, ts in groups.items() if ts}
    ids = [meta[t.key]["eid"] for t in test]
    np.savez_compressed(os.path.join(args.out, method + ".npz"), eids=np.array(ids),
                        lengths=np.array([len(scores[t.key]) for t in test]),
                        scores=np.concatenate([scores[t.key] for t in test]).astype(np.float32),
                        labels=np.concatenate([t.timestamp_labels for t in test]))
    json.dump(dict(rows={g: rows_for(method, ts, scores, thr) for g, ts in groups.items()}, metrics=metrics, thresholds=thr,
                   seconds=time.time() - t0), open(done, "w"))
    print(f"{method} done {time.time() - t0:.0f} s; {metrics}", flush=True)
