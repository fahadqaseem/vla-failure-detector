"""Pure regression of the point of no return score (Prof. Zhu, Nov 13; plan in results/plan_nov13.md, method in docs/method_regression.md).

Target at every policy query = replay failure fraction at that checkpoint (1 - successful replays / K). No t_pnr threshold in training.
Loss = MSE on known points only; every episode has the same total weight (1 / known points per point); no label reweighting.
Leave one task out: train on the other 9 tasks, predict the held-out task. Recoverable failures (pre-check, or scanned with a recoverable
last checkpoint under the 50% rule) are left out of training and evaluation. One run = one policy, one model, one held-out task, one seed.

Models:
  gru_phys_frac     GRU 64 over the last 8 queries of the physical signals -> linear -> sigmoid
  safe_lin          linear probe on features_mean -> sigmoid (as our SAFE-style `safe`, regression target)
  safe_mlp          features_mean -> linear 256 -> ReLU -> linear -> sigmoid
  safe_lstm         PCA 128 of features_mean -> LSTM 128 over the run so far -> linear -> sigmoid
  gru_physvla_frac  GRU 64 over the last 8 queries of [physical signals, PCA 128 of features_mean] -> linear -> sigmoid
  baselines         const (training mean), progress_iso and timer_iso (steps-since-progress / policy step -> isotonic regression)

Writes OUT/{model}/s{seed}/g{G}.json: per held-out episode the steps, targets, K, predictions and t_pnr under the 50% and 70% rules, plus
calib = per-run max scores of the training-task successes, cross-fitted (each training task scored by a model that did not see it).

python scripts/60_regression.py --policy pi05 --model gru_phys_frac --held_out 0 --seed 0 --out data/regression_v2/pi05
"""

import argparse
import glob
import json
import os

import numpy as np
import torch
from scipy.stats import beta
from sklearn.decomposition import PCA
from sklearn.isotonic import IsotonicRegression

p = argparse.ArgumentParser()
p.add_argument("--policy", choices=["oft", "pi05"], required=True)
p.add_argument("--model", required=True, choices=["gru_phys_frac", "safe_lin", "safe_mlp", "safe_lstm", "gru_physvla_frac", "baselines"])
p.add_argument("--held_out", type=int, required=True, help="task held out (0 to 9)")
p.add_argument("--seed", type=int, default=0)
p.add_argument("--out", required=True)
p.add_argument("--epochs", type=int, default=300)
p.add_argument("--lr", type=float, default=1e-3)
p.add_argument("--weight_decay", type=float, default=1e-3)
p.add_argument("--window", type=int, default=8, help="GRU: queries in the memory window")
p.add_argument("--pca_dims", type=int, default=128)
p.add_argument("--progress_m", type=float, default=0.01, help="eef move (m) between queries that counts as progress")
p.add_argument("--smoke", action="store_true", help="test run: 2 epochs, one cross-fit task")
args = p.parse_args()
if args.smoke:
    args.epochs = 2
torch.set_num_threads(int(os.environ.get("OMP_NUM_THREADS", "8")))


# ---- data sets (same pre-registered sets as slurm/n6_train.sbatch) ----
def data_sets(policy):
    if policy == "oft":
        scans = ["data/full_scans/*.json", "data/perturbed_scans/*.json", "data/perturbed_v2_scans/*.json"]
        eps = ["data/natural/*/*.npz", "data/perturbed/task0[0145678]/*.npz"]
        eps += [d + "/*.npz" for d in sorted(glob.glob("data/perturbed_v2/task*")) if os.path.exists(d + "/GATE_PASS")]
        return scans, eps, ["data/perturbed/prechecks", "data/perturbed_v2/prechecks"], "data/week2_refine", "data/physical"
    scans = ["data/pi05/full_scans/*.json", "data/pi05/perturbed_scans/*.json"]
    eps = ["data/pi05/natural/*/*.npz"]
    eps += [d + "/*.npz" for d in sorted(glob.glob("data/pi05/perturbed/task??") + glob.glob("data/pi05/perturbed/task??_s1"))
            if os.path.exists(d + "/GATE_PASS")]  # seeds 0 and 1 only
    return scans, eps, ["data/pi05/perturbed/prechecks"], None, "data/pi05/physical"


def recoverable_50(s):
    """50% rule: Jeffreys lower 0.25 quantile of the success rate >= 0.5 (3 of 4 when K is 4, 10 of 16 when K is 16)."""
    return beta.ppf(0.25, sum(s) + 0.5, len(s) - sum(s) + 0.5) >= 0.5


def recoverable_70(s):
    """70% rule (32_relabel.py): not recoverable if the raw failure fraction is at least 0.7."""
    return 1 - sum(s) / len(s) < 0.7


def t_pnr(scan, ok_rule):
    """First checkpoint from which every later checkpoint is not recoverable; None if the last one is recoverable."""
    ok = [ok_rule(s) for s in scan["successes"]]
    if ok[-1]:
        return None
    i = len(ok) - 1
    while i > 0 and not ok[i - 1]:
        i -= 1
    return int(scan["checkpoints"][i])


def steps_since_progress(eef_q):
    """Queries since the eef last moved more than progress_m between successive queries (RESCUE)."""
    out, count = [0], 0
    for k in range(1, len(eef_q)):
        count = 0 if np.linalg.norm(eef_q[k] - eef_q[k - 1]) > args.progress_m else count + 1
        out.append(count)
    return np.array(out, np.float32)


def load_episodes(policy):
    scan_globs, ep_globs, precheck_dirs, refine_dir, phys_dir = data_sets(policy)
    scans = {}
    for f in [f for g in scan_globs for f in glob.glob(g)]:
        s = json.load(open(f))
        scans[s["episode_id"]] = s
    if refine_dir:  # K 12 more replays at boundary checkpoints: add the counts
        for f in glob.glob(os.path.join(refine_dir, "*.json")):
            r = json.load(open(f))
            s = scans[r["episode_id"]]
            for c, extra in zip(r["checkpoints"], r["successes"]):
                i = s["checkpoints"].index(c)
                s["successes"][i] = list(s["successes"][i]) + list(extra)
    precheck_rec = set()
    for f in [f for d in precheck_dirs for f in glob.glob(os.path.join(d, "*.json"))]:
        pc = json.load(open(f))
        if pc["verdict"] == "recoverable (pre-check)":
            precheck_rec.add(pc["episode_id"])
    episodes, n = [], dict(precheck_recoverable=0, scan_recoverable=0, unscanned_failures=0, induced=0)
    for f in sorted(f for g in ep_globs for f in glob.glob(g)):
        ep = np.load(f, allow_pickle=True)
        eid = os.path.splitext(os.path.basename(f))[0]
        if bool(ep["induced"]):
            n["induced"] += 1
            continue
        success, scan = bool(ep["success"]), scans.get(eid)
        if not success and eid in precheck_rec:
            n["precheck_recoverable"] += 1
            continue
        if not success and scan is None:
            n["unscanned_failures"] += 1
            continue
        if not success and t_pnr(scan, recoverable_50) is None:
            n["scan_recoverable"] += 1
            continue
        assert "features_mean" in ep.files, f"{eid}: no hidden states"
        q = ep["query_steps"].astype(int)
        target, K = np.full(len(q), np.nan, np.float32), np.zeros(len(q), int)
        if scan:
            by_step = {int(c): s for c, s in zip(scan["checkpoints"], scan["successes"])}
            for k, step in enumerate(q):
                if int(step) in by_step:
                    s = by_step[int(step)]
                    target[k], K[k] = 1 - sum(s) / len(s), len(s)
        if success and not scan:
            target[:] = 0.0  # assumption: a successful run is safe at every query (K 0 = assumed, noise floor 0)
        phys = np.load(os.path.join(phys_dir, eid + ".npz"))["x"].astype(np.float32)
        assert len(phys) == len(q), eid
        episodes.append(dict(
            eid=eid, task=int(ep["task_id"]), success=success, scanned=scan is not None, steps=q, target=target, K=K,
            t50=None if success else t_pnr(scan, recoverable_50), t70=None if success else t_pnr(scan, recoverable_70),
            source="perturbed" if "perturbed" in ep.files else "natural",
            feat=ep["features_mean"].astype(np.float32), phys=phys,
            progress=steps_since_progress(ep["eef"][q]), timer=q.astype(np.float32)))
    n.update(kept_episodes=len(episodes), kept_failures=sum(not e["success"] for e in episodes),
             kept_successes=sum(e["success"] for e in episodes), known_points=int(sum((~np.isnan(e["target"])).sum() for e in episodes)))
    return episodes, n


# ---- models ----
def windows(X, n):
    """(queries, d) -> (queries, n, d): the last n queries at each query; earlier ones repeat the first."""
    idx = np.maximum(np.arange(len(X))[:, None] - np.arange(n - 1, -1, -1)[None, :], 0)
    return X[idx]


def weights_and_targets(rows):
    """Known points only. Each episode has the same total weight: 1 / (known points in it)."""
    y, w = [], []
    for e in rows:
        m = ~np.isnan(e["target"])
        y.append(e["target"][m])
        w.append(np.full(m.sum(), 1.0 / m.sum(), np.float32))
    w = np.concatenate(w)
    return np.concatenate(y), w / w.sum()


class GRUNet(torch.nn.Module):
    def __init__(self, d, h=64):
        super().__init__()
        self.rnn, self.out = torch.nn.GRU(d, h, batch_first=True), torch.nn.Linear(h, 1)

    def forward(self, x):  # (points, window, d) -> (points,)
        return self.out(self.rnn(x)[1][-1]).squeeze(1)


class LSTMNet(torch.nn.Module):
    def __init__(self, d, h=128):
        super().__init__()
        self.rnn, self.out = torch.nn.LSTM(d, h, batch_first=True), torch.nn.Linear(h, 1)

    def forward(self, x):  # (episodes, queries, d), padded at the end -> (episodes, queries)
        return self.out(self.rnn(x)[0]).squeeze(2)


def per_query_input(model, e, pca):
    if model == "gru_phys_frac":
        return e["phys"]
    if model == "gru_physvla_frac":
        return np.concatenate([e["phys"], pca.transform(e["feat"]).astype(np.float32)], 1)
    if model == "safe_lstm":
        return pca.transform(e["feat"]).astype(np.float32)
    return e["feat"]  # safe_lin, safe_mlp


def train(model, rows, seed):
    """Fit one model on these episodes. Returns a function: episode -> prediction at every query."""
    torch.manual_seed(seed)
    pca = None
    if model in ("gru_physvla_frac", "safe_lstm"):
        pca = PCA(args.pca_dims, random_state=seed).fit(np.concatenate([e["feat"] for e in rows]))
    inputs = [per_query_input(model, e, pca) for e in rows]
    flat = np.concatenate(inputs)
    mu, sd = flat.mean(0), flat.std(0) + 1e-6
    del flat
    std = lambda x: ((x - mu) / sd).astype(np.float32)  # noqa: E731
    y, w = map(torch.tensor, weights_and_targets(rows))
    masks = [~np.isnan(e["target"]) for e in rows]
    d = mu.shape[0]
    if model == "safe_lstm":
        net = LSTMNet(d)
        X = torch.nn.utils.rnn.pad_sequence([torch.tensor(std(x)) for x in inputs], batch_first=True)
        M = torch.nn.utils.rnn.pad_sequence([torch.tensor(m) for m in masks], batch_first=True)
        predict_train = lambda: net(X)[M]  # noqa: E731  (row order = episode order, query order, same as y)
    else:
        if model.startswith("gru"):
            net = GRUNet(d)
            X = torch.tensor(np.concatenate([windows(std(x), args.window)[m] for x, m in zip(inputs, masks)]))
        else:
            net = torch.nn.Linear(d, 1) if model == "safe_lin" else torch.nn.Sequential(
                torch.nn.Linear(d, 256), torch.nn.ReLU(), torch.nn.Linear(256, 1))
            X = torch.tensor(np.concatenate([std(x)[m] for x, m in zip(inputs, masks)]))
        predict_train = lambda: net(X).reshape(-1)  # noqa: E731
    del inputs
    opt = torch.optim.Adam(net.parameters(), lr=args.lr, weight_decay=args.weight_decay)
    for _ in range(args.epochs):  # full batch
        loss = (w * (torch.sigmoid(predict_train()) - y) ** 2).sum()
        opt.zero_grad()
        loss.backward()
        opt.step()
    net.eval()

    def score(e):
        x = std(per_query_input(model, e, pca))
        with torch.no_grad():
            if model == "safe_lstm":
                return torch.sigmoid(net(torch.tensor(x)[None]))[0].numpy()
            if model.startswith("gru"):
                return torch.sigmoid(net(torch.tensor(windows(x, args.window)))).numpy()
            return torch.sigmoid(net(torch.tensor(x)).reshape(-1)).numpy()
    return score


def train_baseline(name, rows):
    y, w = weights_and_targets(rows)
    if name == "const":
        c = float((w * y).sum())
        return lambda e: np.full(len(e["steps"]), c, np.float32)
    key = name.removesuffix("_iso")  # progress or timer
    x = np.concatenate([e[key][~np.isnan(e["target"])] for e in rows])
    iso = IsotonicRegression(increasing=True, y_min=0.0, y_max=1.0, out_of_bounds="clip").fit(x, y, sample_weight=w)
    return lambda e: iso.predict(e[key]).astype(np.float32)


def fit(name, rows):
    return train_baseline(name, rows) if name in ("const", "progress_iso", "timer_iso") else train(name, rows, args.seed)


# ---- one held-out task ----
episodes, counts = load_episodes(args.policy)
print(args.policy, json.dumps(counts))
train_eps = [e for e in episodes if e["task"] != args.held_out]
test_eps = [e for e in episodes if e["task"] == args.held_out]
train_tasks = sorted({e["task"] for e in train_eps})
names = ["const", "progress_iso", "timer_iso"] if args.model == "baselines" else [args.model]
for name in names:
    score = fit(name, train_eps)
    calib = []  # cross-fitted per-run max of the training-task successes (backup alarm thresholds)
    for u in train_tasks[:1] if args.smoke else train_tasks:
        score_u = fit(name, [e for e in train_eps if e["task"] != u])
        calib += [[e["eid"], float(score_u(e).max())] for e in train_eps if e["task"] == u and e["success"]]
    rows = [dict(eid=e["eid"], task=e["task"], success=e["success"], scanned=e["scanned"], source=e["source"],
                 steps=e["steps"].tolist(), target=[None if np.isnan(t) else float(t) for t in e["target"]], K=e["K"].tolist(),
                 pred=[float(v) for v in score(e)], t50=e["t50"], t70=e["t70"]) for e in test_eps]
    d = os.path.join(args.out, name, f"s{args.seed}")
    os.makedirs(d, exist_ok=True)
    json.dump(dict(policy=args.policy, model=name, seed=args.seed, held_out=args.held_out, counts=counts, rows=rows, calib=calib,
                   params={k: v for k, v in vars(args).items() if k not in ("out", "held_out", "model")}),
              open(os.path.join(d, f"g{args.held_out}.json"), "w"))
    print(f"{name} g{args.held_out}: {len(rows)} test episodes, {len(calib)} calibration successes")
