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
  combined  same MLP and loss on more inputs (Fahad, Oct 18): the inputs above plus motion signals
            (eef displacement over the last 4 chunks, its length, the steps-since-progress value) plus a
            window of the last 4 queries as averaged deltas (features_mean and action chunk minus their mean
            over the 3 previous queries; zero at the first query). Still no step index.

  mlp_reg, combined_reg  regularised variants (Fahad, Oct 20): the 4096 VLA features (and, in combined_reg, their
            averaged deltas) go through PCA to --pca_dims (128) fitted on the training rows only (deltas use the same
            components, no centring); dropout 0.3 after the ReLU; early stopping on an inner validation split (20% of
            the training episodes, failures with a t_pnr split separately), patience 30 epochs, best epoch kept.

  gated_mlp, gated_combined  gated rule (Fahad, Oct 20): alarm only where the progress baseline alarms AND the learned
            model's risk is above its threshold. Gate = progress above its own conformal threshold at --gate_alpha (20%,
            from the training successes); score = the model's risk where the gate is open, -inf elsewhere. The usual
            thresholds are then set on this score, so false alarms on successes stay at the limit (5%).

  privileged diagnostic (Fahad, Oct 19; only with --privileged): same MLP and loss, but the inputs are
            simulator poses instead of VLA features (scripts/10_privileged_features.py: eef, fingers, gripper
            counter, goal object minus target and minus eef, goal predicates true now). Shows how far the
            labels can be predicted when the state is known exactly.

Two options for unseen tasks (Fahad, Oct 19; both change the inputs of every model that reads features):
  --task_embed FILE    task conditioning: append the task's instruction embedding (scripts/11_task_embedding.py,
                       mean of the VLA's last-layer hidden states over the instruction tokens, 4096) to the inputs.
  --task_norm_steps N  per-task normalisation: standardise features_mean with the mean and std of that task's
                       successful runs over their first N steps (queries at step < N). No labels needed, so the
                       held-out task can use its own successes; every training task uses its own.

Leave-one-task-out: for each task, train on the other 9 and test on it.
--split episode (diagnostic, Fahad Oct 19, "seen tasks"): instead hold out episodes, 5 folds by
initial-state index (episode_idx % 5) within every task, so every task is seen in training.
Thresholds, both from the cross-fitted scores of all training-group successes, at each false-alarm limit in --alphas
(5%, 10%, 20%; the headline table uses --alpha):
  fixed          one number: conformal quantile of the per-run maximum score.
  time-varying   SAFE-style functional conformal band (Fahad, Oct 20): per 64-step bin, the mean and std of the
                 success scores from half of the calibration runs; the other half gives c = conformal quantile of
                 the per-run max of (score - mean(bin)) / std(bin); threshold(bin) = mean + c std. Bins with fewer
                 than --min_runs_per_bin runs (successes rarely last long) reuse the last bin that has enough.
Conformal threshold from ALL successes of the 9 training tasks. Their scores must come from a model that
did not see their task (as at test time), so they are cross-fitted: for each training task u, a model
trained on the other 8 tasks scores u's successes. Threshold = the ceil((n+1)(1-alpha))-th smallest
per-run max score over the n calibration runs. Alarm = first query step whose score is above it.
False alarms are measured on ALL successes of the held-out task.

Metrics (pooled over the held-out groups: 10 tasks, or 5 episode folds):
  AUROC per step over the whole run (sklearn); time-matched AUROC: positive steps (label 1) are compared
  only with steps of successful runs in the same 64-step time bin (pairs from different bins are not
  counted; bins without both are skipped), so knowing how long the run has lasted helps much less;
  unnecessary alarms = alarms on failures that stayed recoverable (no t_pnr) and on successes;
  false-alarm rate on held-out successes;
  on labelled failures with t_pnr > 0 (doomed-from-start episodes, t_pnr = 0, are left out of timing):
  recall (any alarm), timely (alarm at or before t_pnr, RESCUE-style), late (after), missed,
  lead time = t_pnr - t_alarm (positive = early), mean |t_alarm - t_pnr|, median eta = t_alarm / t_pnr.

python scripts/06_train_predictor.py --scans "data/full_scans/*.json" --episodes "data/natural/*/*.npz" --out results/predictor
With perturbed-natural episodes added (scans, plus pre-check "recoverable" failures labelled 0 everywhere):
python scripts/06_train_predictor.py --scans "data/full_scans/*.json" "data/perturbed_scans/*.json" \
    --episodes "data/natural/*/*.npz" "data/perturbed/*/*.npz" --prechecks data/perturbed/prechecks \
    --out results/predictor_with_perturbed
"""

import argparse
import glob
import json
import os

import numpy as np
import torch
from sklearn.decomposition import PCA
from sklearn.metrics import roc_auc_score

p = argparse.ArgumentParser()
p.add_argument("--scans", nargs="+", default=["data/full_scans/*.json"])
p.add_argument("--episodes", nargs="+", default=["data/natural/*/*.npz"])
p.add_argument("--prechecks", default=None, help="09_precheck.py results: failures marked recoverable get label 0")
p.add_argument("--bin", type=int, default=64, help="time bin (steps) for the time-matched AUROC")
p.add_argument("--tau_min_success", type=int, default=3, help="recoverable if >= this many of K=4 replays succeed (tau 0.5)")
p.add_argument("--alpha", type=float, default=0.05, help="target false-alarm rate on successful runs (headline)")
p.add_argument("--alphas", nargs="+", type=float, default=[0.05, 0.10, 0.20], help="false-alarm limits reported")
p.add_argument("--min_runs_per_bin", type=int, default=20, help="time-varying threshold: runs needed in a bin")
p.add_argument("--pca_dims", type=int, default=128, help="regularised models: PCA size of the VLA features")
p.add_argument("--dropout", type=float, default=0.3, help="regularised models: dropout after the ReLU")
p.add_argument("--val_frac", type=float, default=0.2, help="regularised models: inner validation episodes")
p.add_argument("--patience", type=int, default=30, help="regularised models: epochs without validation gain")
p.add_argument("--gate_alpha", type=float, default=0.20, help="gated models: false-alarm limit of the progress gate")
p.add_argument("--progress_m", type=float, default=0.01, help="eef move (m) between boundaries that counts as progress")
p.add_argument("--epochs", type=int, default=300)
p.add_argument("--lr", type=float, default=1e-3)
p.add_argument("--weight_decay", type=float, default=1e-3)
p.add_argument("--hidden", type=int, default=256)
p.add_argument("--seed", type=int, default=0)
p.add_argument("--split", choices=["task", "episode"], default="task",
               help="task = leave-one-task-out; episode = 5 folds by episode_idx %% 5 within each task (seen tasks)")
p.add_argument("--folds", type=int, default=5)
p.add_argument("--privileged", default=None, help="dir of 10_privileged_features.py outputs: adds the privileged model")
p.add_argument("--models", nargs="+", default=None, help="subset of models to run (default: all)")
p.add_argument("--task_embed", default=None, help="npz from 11_task_embedding.py: append the task embedding to the inputs")
p.add_argument("--task_norm_steps", type=int, default=0,
               help="if > 0: standardise features_mean per task with its successes' queries at step < this")
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


def motion_and_window(eef_q, progress, feats, chunks, n=4):
    """Inputs added for the combined model, per query k (only queries k-3 .. k are used):
    motion = eef displacement since query k-3 (3), its length (1), steps-since-progress (1);
    dfeat, dchunk = features_mean and action chunk minus their mean over queries k-3 .. k-1 (zero at k = 0)."""
    disp, dfeat, dchunk = [], [], []
    for k in range(len(eef_q)):
        j = max(0, k - (n - 1))
        disp.append(eef_q[k] - eef_q[j])
        prev = slice(j, k) if k > 0 else slice(0, 1)
        dfeat.append(feats[k] - feats[prev].mean(0))
        dchunk.append(chunks[k] - chunks[prev].mean(0))
    disp = np.array(disp)
    motion = np.concatenate([disp, np.linalg.norm(disp, axis=1, keepdims=True), progress[:, None]], axis=1)
    return motion.astype(np.float32), np.array(dfeat, np.float32), np.array(dchunk, np.float32)


# ---- load episodes ----
scans = {}
for f in [f for pat in args.scans for f in glob.glob(pat)]:
    s = json.load(open(f))
    scans[s["episode_id"]] = s
precheck_recoverable = set()
if args.prechecks:
    for f in glob.glob(os.path.join(args.prechecks, "*.json")):
        pc = json.load(open(f))
        if pc["verdict"] == "recoverable (pre-check)":
            precheck_recoverable.add(pc["episode_id"])

files = sorted(f for pat in args.episodes for f in glob.glob(pat))
task_norm = {}  # task -> (mean, std) of features_mean over the first task_norm_steps of its successful runs
if args.task_norm_steps > 0:
    early = {}
    for f in files:
        ep = np.load(f, allow_pickle=True)
        if bool(ep["success"]) and not bool(ep["induced"]):
            early.setdefault(int(ep["task_id"]), []).append(
                ep["features_mean"][ep["query_steps"] < args.task_norm_steps].astype(np.float32))
    for t, rows in early.items():
        X = np.concatenate(rows)
        task_norm[t] = (X.mean(0), X.std(0) + 1e-6)
task_embed = None
if args.task_embed:
    te = np.load(args.task_embed)
    task_embed = dict(zip(te["task_ids"].tolist(), te["emb"]))

episodes = []  # one dict per episode
for f in files:
    ep = np.load(f, allow_pickle=True)
    if bool(ep["induced"]):
        continue
    eid = os.path.splitext(os.path.basename(f))[0]
    success, scan = bool(ep["success"]), scans.get(eid)
    q = ep["query_steps"].astype(int)
    actions = ep["actions"]
    chunks = np.stack([actions[s:s + 8].reshape(-1) if s + 8 <= len(actions)
                       else np.pad(actions[s:], ((0, s + 8 - len(actions)), (0, 0))).reshape(-1) for s in q])
    feats = ep["features_mean"].astype(np.float32)
    if task_norm:
        mu_t, sd_t = task_norm[int(ep["task_id"])]
        feats = (feats - mu_t) / sd_t
    x_rest = np.concatenate([chunks, ep["eef"][q], ep["query_grippers"]], axis=1).astype(np.float32)
    if task_embed is not None:
        x_rest = np.concatenate([x_rest, np.tile(task_embed[int(ep["task_id"])], (len(q), 1))], axis=1)
    x = np.concatenate([feats, x_rest], axis=1)
    progress = steps_since_progress(ep["eef"][q])
    motion, dfeat, dchunk = motion_and_window(ep["eef"][q], progress, feats, chunks)
    x_comb = np.concatenate([x, motion, dfeat, dchunk], axis=1)
    x_priv = np.load(os.path.join(args.privileged, eid + ".npz"))["x"] if args.privileged else None
    t_pnr = t_pnr_from_scan(scan) if scan else None
    pre_rec = eid in precheck_recoverable and not success and not scan  # label 0 everywhere, no risk target
    label = np.zeros(len(q), np.float32) if t_pnr is None else (q >= t_pnr).astype(np.float32)
    risk = np.full(len(q), np.nan, np.float32)
    if scan:
        by_step = {c: 1 - sum(s) / len(s) for c, s in zip(scan["checkpoints"], scan["successes"])}
        risk = np.array([by_step.get(int(s), np.nan) for s in q], np.float32)
    group = int(ep["task_id"]) if args.split == "task" else int(ep["episode_idx"]) % args.folds
    episodes.append(dict(eid=eid, task=int(ep["task_id"]), group=group, success=success, scanned=scan is not None or pre_rec,
                         source="perturbed" if "perturbed" in ep.files else "natural",
                         t_pnr=t_pnr, doomed=t_pnr == 0, steps=q, x=x, x_comb=x_comb, x_priv=x_priv, label=label, risk=risk,
                         feat=feats, x_rest=x_rest, motion=motion, dfeat=dfeat, dchunk=dchunk,
                         progress=progress))

labelled = [e for e in episodes if e["scanned"] or e["success"]]
for src in ["natural", "perturbed"]:
    es = [e for e in labelled if e["source"] == src]
    if es:
        print(f"{src}: {sum(not e['success'] for e in es)} labelled failures "
              f"({sum(not e['success'] and e['t_pnr'] is None for e in es)} recoverable, "
              f"{sum(e['eid'] in precheck_recoverable for e in es)} of them by pre-check), {sum(e['success'] for e in es)} successes")
n_fail_lab = sum(not e["success"] and e["scanned"] for e in episodes)
print(f"{len(episodes)} natural episodes; labelled: {len(labelled)} "
      f"({n_fail_lab} scanned failures, {sum(e['success'] for e in labelled)} successes, "
      f"{sum(e['doomed'] for e in episodes)} doomed from start)")


# ---- models ----
def reg_inputs(e, model_name, pca):
    """Inputs of the regularised models: PCA of the VLA features, then the other inputs unchanged."""
    parts = [pca.transform(e["feat"]), e["x_rest"]]
    if model_name == "combined_reg":
        parts += [e["motion"], e["dfeat"] @ pca.components_.T, e["dchunk"]]
    return np.concatenate(parts, axis=1).astype(np.float32)


def targets(rows, model_name):
    """Label, risk (nan where not scanned) and weight per row."""
    if model_name == "safe":
        y = np.concatenate([np.full(len(e["steps"]), float(not e["success"]), np.float32) for e in rows])
        r = np.full_like(y, np.nan)
    else:
        y = np.concatenate([e["label"] for e in rows])
        r = np.concatenate([e["risk"] for e in rows])
    # Each episode weighs the same; then positives and negatives get the same total weight.
    w = np.concatenate([np.full(len(e["steps"]), 1 / len(e["steps"]), np.float32) for e in rows])
    w[y == 1] *= w[y == 0].sum() / max(w[y == 1].sum(), 1e-12)
    return torch.tensor(y), torch.tensor(r), torch.tensor(w / w.sum())


def loss_fn(logit, y, r, w):
    loss = (w * torch.nn.functional.binary_cross_entropy_with_logits(logit, y, reduction="none")).sum()
    has_risk = ~torch.isnan(r)
    if has_risk.any():
        wr = w[has_risk] / w[has_risk].sum()
        loss = loss + (wr * (torch.sigmoid(logit[has_risk]) - r[has_risk]) ** 2).sum()
    return loss


def train(rows, model_name):
    """rows: list of episodes. Returns a function: episode -> per-step score."""
    torch.manual_seed(args.seed)
    regularised = model_name.endswith("_reg")
    if regularised:
        pca = PCA(args.pca_dims, random_state=args.seed).fit(np.concatenate([e["feat"] for e in rows]))
        inputs = lambda e: reg_inputs(e, model_name, pca)  # noqa: E731
    else:
        key = {"combined": "x_comb", "privileged": "x_priv"}.get(model_name, "x")
        inputs = lambda e: e[key]  # noqa: E731
    X_all = np.concatenate([inputs(e) for e in rows])
    mu, sd = X_all.mean(0), X_all.std(0) + 1e-6
    tensor = lambda es: torch.tensor((np.concatenate([inputs(e) for e in es]) - mu) / sd)  # noqa: E731
    fit_rows, val_rows = rows, []
    if regularised:  # inner validation split by episode; episodes with label-1 steps are split separately
        rng = np.random.default_rng(args.seed)
        fit_rows = []
        for group in ([e for e in rows if e["label"].any()], [e for e in rows if not e["label"].any()]):
            order = rng.permutation(len(group))
            n_val = int(round(args.val_frac * len(group)))
            val_rows += [group[i] for i in order[:n_val]]
            fit_rows += [group[i] for i in order[n_val:]]
    X, (y, r, w) = tensor(fit_rows), targets(fit_rows, model_name)
    d = X.shape[1]
    if model_name in ("logreg", "safe"):
        net = torch.nn.Linear(d, 1)
    else:
        layers = [torch.nn.Linear(d, args.hidden), torch.nn.ReLU()]
        if regularised:
            layers.append(torch.nn.Dropout(args.dropout))
        net = torch.nn.Sequential(*layers, torch.nn.Linear(args.hidden, 1))
    opt = torch.optim.Adam(net.parameters(), lr=args.lr, weight_decay=args.weight_decay)
    if val_rows:
        X_val, (y_val, r_val, w_val) = tensor(val_rows), targets(val_rows, model_name)
        best_loss, best_epoch, best_state = np.inf, 0, None
    for epoch in range(args.epochs):  # full batch
        net.train()
        loss = loss_fn(net(X).squeeze(1), y, r, w)
        opt.zero_grad()
        loss.backward()
        opt.step()
        if val_rows:
            net.eval()
            with torch.no_grad():
                v = loss_fn(net(X_val).squeeze(1), y_val, r_val, w_val).item()
            if v < best_loss:
                best_loss, best_epoch = v, epoch
                best_state = {k: t.clone() for k, t in net.state_dict().items()}
            elif epoch - best_epoch >= args.patience:
                break
    if val_rows:
        net.load_state_dict(best_state)
        stopped_at.append(best_epoch + 1)
    net.eval()

    def score(e):
        with torch.no_grad():
            return torch.sigmoid(net(torch.tensor((inputs(e) - mu) / sd)).squeeze(1)).numpy()
    return score


stopped_at = []  # best epoch of every regularised fit (reported in the summary)


fitted = {}  # (model, training episodes) -> score function, so the gated models reuse the mlp / combined fits


def fit(model_name, train_eps):
    """Train on these episodes (or nothing, for the rule-based baselines)."""
    key = (model_name, frozenset(e["eid"] for e in train_eps))
    if key not in fitted:
        fitted[key] = fit_new(model_name, train_eps)
    return fitted[key]


def fit_new(model_name, train_eps):
    if model_name.startswith("gated_"):
        risk = fit(model_name[len("gated_"):], train_eps)
        gate = conformal_threshold([e["progress"].max() for e in train_eps if e["success"]], args.gate_alpha)
        return lambda e: np.where(e["progress"] > gate, risk(e), -np.inf)
    if model_name == "timer":
        return lambda e: e["steps"].astype(np.float32)
    if model_name == "progress":
        return lambda e: e["progress"]
    if model_name == "safe":
        return train(train_eps, "safe")
    return train([e for e in train_eps if e["scanned"] or e["success"]], model_name)


def conformal_threshold(run_maxes, alpha):
    n = len(run_maxes)
    k = int(np.ceil((n + 1) * (1 - alpha)))
    return np.inf if k > n else float(np.sort(run_maxes)[k - 1])


def fixed_threshold(calib, alpha):
    """calib: list of (steps, scores) of calibration successes. Returns steps -> threshold per step."""
    thr = conformal_threshold([s.max() for _, s in calib], alpha)
    return lambda steps: np.full(len(steps), thr)


def time_varying_threshold(calib, alpha):
    """SAFE-style band: mean + c std per time bin (see the top of this file)."""
    fit_half, cal_half = calib[0::2], calib[1::2]
    n_bins = max(int(st.max()) for st, _ in calib) // args.bin + 1
    mean, std = np.zeros(n_bins), np.ones(n_bins)
    last_ok = 0
    for b in range(n_bins):
        in_bin = [s[(st // args.bin == b) & np.isfinite(s)] for st, s in fit_half]  # -inf = gate closed
        in_bin = [v for v in in_bin if len(v)]
        if len(in_bin) >= args.min_runs_per_bin:
            v = np.concatenate(in_bin)
            mean[b], std[b], last_ok = v.mean(), v.std() + 1e-6, b
        else:
            mean[b], std[b] = mean[last_ok], std[last_ok]
    bins = lambda steps: np.minimum(np.asarray(steps) // args.bin, n_bins - 1)  # noqa: E731
    # Bins past the calibration data reuse the last bin.
    c = conformal_threshold([((s - mean[bins(st)]) / std[bins(st)]).max() for st, s in cal_half], alpha)
    return lambda steps: mean[bins(steps)] + c * std[bins(steps)]


THRESHOLDS = {"fixed": fixed_threshold, "time-varying": time_varying_threshold}


def first_alarm(e, s, thr):
    """thr: one threshold per step."""
    above = np.nonzero(s > thr)[0]
    return int(e["steps"][above[0]]) if len(above) else None


def alarm_key(mode, alpha):
    return f"{mode} {alpha:.2f}"


# ---- leave-one-group-out: group = task (default), or episode fold (--split episode) ----
models = (["timer", "progress", "safe", "logreg", "mlp", "combined", "mlp_reg", "combined_reg", "gated_mlp", "gated_combined"]
          + (["privileged"] if args.privileged else []))
alphas = sorted(set(args.alphas) | {args.alpha})
headline = alarm_key("fixed", args.alpha)
models = [m for m in models if args.models is None or m in args.models]
rows_out = []  # one row per (model, held-out episode)
groups = sorted({e["group"] for e in episodes})
for test_group in groups:
    train_groups = [t for t in groups if t != test_group]
    train_eps = [e for e in episodes if e["group"] != test_group]
    test = [e for e in labelled if e["group"] == test_group]
    for m in models:
        # Calibration scores for each training group's successes, from a model that did not see that group.
        calib = []  # (steps, scores) of every training-group success
        for u in train_groups:
            score_u = fit(m, [e for e in train_eps if e["group"] != u])
            calib += [(e["steps"], score_u(e)) for e in train_eps if e["group"] == u and e["success"]]
        thresholds = {alarm_key(mode, a): make(calib, a) for mode, make in THRESHOLDS.items() for a in alphas}
        score = fit(m, train_eps)
        for e in test:
            s = score(e)
            alarms = {k: first_alarm(e, s, thr(e["steps"])) for k, thr in thresholds.items()}
            rows_out.append(dict(model=m, task=e["task"], group=test_group, eid=e["eid"], success=e["success"], t_pnr=e["t_pnr"],
                                 doomed=e["doomed"], t_alarm=alarms[headline], alarms=alarms,
                                 threshold=float(thresholds[headline](e["steps"][:1])[0]),
                                 labels=e["label"].tolist(), scores=s.tolist(), steps=e["steps"].tolist()))
    print(f"held-out {args.split} group {test_group}: {len(train_eps)} training episodes, {len(test)} test episodes", flush=True)


# ---- metrics ----
def summarise(rows, key=None):
    """key: which alarm (threshold mode and false-alarm limit); default the headline one."""
    rows = [dict(r, t_alarm=r["alarms"][key]) for r in rows] if key else rows
    labels = np.concatenate([r["labels"] for r in rows])
    scores = np.concatenate([r["scores"] for r in rows])
    finite = np.isfinite(scores)  # gated models: -inf where the gate is closed, ranked below every other step
    scores = np.where(finite, scores, scores[finite].min() - 1 if finite.any() else 0.0)
    auroc = roc_auc_score(labels, scores) if 0 < labels.sum() < len(labels) else float("nan")
    # Time-matched AUROC: label-1 steps against success steps of the same time bin, weighted by pairs.
    steps = np.concatenate([r["steps"] for r in rows]) // args.bin
    is_succ = np.concatenate([np.full(len(r["steps"]), r["success"]) for r in rows])
    tm_sum, tm_pairs = 0.0, 0
    for b in np.unique(steps):
        pos, neg = scores[(steps == b) & (labels == 1)], scores[(steps == b) & is_succ]
        if len(pos) and len(neg):
            auc = roc_auc_score(np.r_[np.ones(len(pos)), np.zeros(len(neg))], np.r_[pos, neg])
            tm_sum, tm_pairs = tm_sum + auc * len(pos) * len(neg), tm_pairs + len(pos) * len(neg)
    succ = [r for r in rows if r["success"]]
    timed = [r for r in rows if not r["success"] and r["t_pnr"] not in (None, 0)]
    recov = [r for r in rows if not r["success"] and r["t_pnr"] is None]
    alarmed = [r for r in timed if r["t_alarm"] is not None]
    lead = [r["t_pnr"] - r["t_alarm"] for r in alarmed]
    return dict(
        auroc=auroc, auroc_time_matched=tm_sum / tm_pairs if tm_pairs else float("nan"),
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
lines = ["# Per-step t_pnr predictor, " + ("leave-one-task-out" if args.split == "task" else
         f"SEEN TASKS: {args.folds} folds by episode_idx % {args.folds} within each task (diagnostic)"), "",
         f"Labels: full replay scans, K 4, tau 0.5 (>= {args.tau_min_success} of 4 succeed = recoverable). "
         f"Scanned failures: {n_fail_lab}; doomed from start (t_pnr 0, left out of timing): "
         f"{sum(e['doomed'] for e in episodes)}. Training and test use all natural successes. "
         f"Threshold (headline table): fixed conformal, alpha {args.alpha}, from cross-fitted scores of all training-group successes. "
         f"epochs {args.epochs}, lr {args.lr}, weight decay {args.weight_decay}, hidden {args.hidden}, seed {args.seed}, "
         f"progress {args.progress_m} m."
         + (f" Task embedding appended: {args.task_embed}." if args.task_embed else "")
         + (f" Per-task normalisation of features_mean: first {args.task_norm_steps} steps of each task's successes."
            if args.task_norm_steps else ""),
         "", "Timely = alarm at or before t_pnr; late = after; lead = t_pnr - t_alarm (positive = early); "
         "|err| = mean |t_alarm - t_pnr|; all over alarmed failures with t_pnr > 0. "
         f"Time-matched AUROC: label-1 steps vs success steps in the same {args.bin}-step bin only. "
         "Unnecessary alarms on recoverable failures = alarms on failures that never pass a t_pnr.", "",
         "Episodes: " + "; ".join(f"{src}: {sum(e['source'] == src and not e['success'] for e in labelled)} labelled failures, "
                                  f"{sum(e['source'] == src and e['success'] for e in labelled)} successes"
                                  for src in ["natural", "perturbed"] if any(e["source"] == src for e in labelled))
         + " (pooled in every number below).", "",
         "| model | unnecessary alarms on recoverable failures | false alarms on successes | per-step AUROC | time-matched AUROC | failures with t_pnr > 0 | recall | timely | late | missed | median lead (steps) | mean abs err (steps) | median eta |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
for m in models:
    s = summarise([r for r in rows_out if r["model"] == m])
    lines.append(f"| {m} | {s['alarms_on_recoverable_fail']} of {s['n_recoverable_fail']} | {s['false_alarm']:.3f} (of {s['n_success']}) | "
                 f"{s['auroc']:.3f} | {s['auroc_time_matched']:.3f} | {s['n_timed']} | {s['recall']:.2f} | "
                 f"{s['timely']} | {s['late']} | {s['missed']} | {s['median_lead']:.1f} | {s['mean_abs_err']:.1f} | "
                 f"{s['median_eta']:.2f} |")
lines += ["", "Timely alarms (at or before t_pnr) / late / missed of the failures with t_pnr > 0, and false alarms on "
          "successes, for each threshold and false-alarm limit:", "",
          "| model | " + " | ".join(f"{mode} {a:.0%}" for mode in THRESHOLDS for a in alphas) + " |",
          "|---|" + "---|" * (len(THRESHOLDS) * len(alphas))]
for m in models:
    cells = []
    for mode in THRESHOLDS:
        for a in alphas:
            s = summarise([r for r in rows_out if r["model"] == m], alarm_key(mode, a))
            cells.append(f"{s['timely']} / {s['late']} / {s['missed']}, FA {s['false_alarm']:.3f}")
    lines.append(f"| {m} | " + " | ".join(cells) + " |")
if stopped_at:
    lines += ["", f"Regularised fits: best epoch median {int(np.median(stopped_at))}, range {min(stopped_at)} to "
              f"{max(stopped_at)} ({len(stopped_at)} fits)."]
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
    json.dump([{k: v for k, v in r.items() if k not in ("labels", "scores", "steps")} for r in rows_out], f, indent=1)
# Per-step scores of the held-out failures (for figures), with their query steps.
with open(os.path.join(args.out, "failure_scores.json"), "w") as f:
    json.dump([r for r in rows_out if not r["success"]], f)
print(text)
