"""Bio-inspired precursor features per query (pnr_probe experiment, Oct 27 2026), from saved data only (CPU).

Reads the episodes and the Track 1 physical signals (scripts/20_physical_signals.py, 33 numbers per query).
Writes one file per episode and feature set, same format as 20_physical_signals.py (x, names, query_steps), so
scripts/06_train_predictor.py reads them unchanged with --phys DIR (models mlp_phys, gru_phys).

Feature sets (every value at query t uses only data available at query t; never the step index):
  surprise  forward model (MLP 64, scikit-learn) predicting the change of 22 physical state numbers (goal object
            distances, positions, height, tilt, contact, goal distance, gripper opening, eef) from query t-1 to t,
            from the 33 physical numbers and the action chunk at t-1; trained on successes only.
            Error = squared error in standardised units: total and per group (eef, gripper, contact, objects),
            plus their rolling mean over the last 4 queries (10 numbers; 0 at the first query).
  csd       critical slowing down: rolling variance and lag-1 autocorrelation over the last 4 and 8 queries of the
            surprise total, the 22 physical numbers and a PCA-16 of the VLA features_mean (156 numbers).
  ttc       time-to-contact per goal slot (2 objects, 1 articulated fixture): distance / closing speed in queries,
            capped at 50 (also when not closing), as log(1 + ttc), plus a closing flag (6 numbers).
  micro     counts over the last 8 queries: contact flicker (contact on/off changes, goal slots summed), gripper
            close-reopen (close command followed by open, from the executed actions), jerk spikes (eef third
            difference above the 99th percentile of fitting successes) (3 numbers).
  bio       surprise + csd + ttc + micro.         bioplus   bio + the 33 Track 1 physical numbers.
Joint torques are not in the saved data (sim states hold qpos / qvel only), so they are not used.

Cross-fitting: everything fitted (forward model, PCA, jerk threshold) is fitted on successes OUTSIDE the episode's
group and then applied to that group. Groups = task (--split task, leave-one-task-out) or episode_idx % 5
(--split episode, seen tasks), the same groups as 06_train_predictor.py. So no feature of an episode comes from a
model that saw its task (or fold).

python pnr_probe/precursor_features.py --split task --out pnr_probe/data/unseen
"""

import argparse
import glob
import os

import numpy as np
from sklearn.decomposition import PCA
from sklearn.neural_network import MLPRegressor

D = os.path.expanduser("~/vla-failure-detector/data")
p = argparse.ArgumentParser()
p.add_argument("--episodes", nargs="+", default=[f"{D}/natural/*/*.npz", f"{D}/perturbed/task0[0145678]/*.npz",
                                                  f"{D}/perturbed_v2/task0[0147]/*.npz"])
p.add_argument("--phys", default=f"{D}/physical")
p.add_argument("--split", choices=["task", "episode"], default="task")
p.add_argument("--folds", type=int, default=5)
p.add_argument("--out", required=True)
p.add_argument("--seed", type=int, default=0)
args = p.parse_args()

SLOT = ["dist", "ddist", "pos_x", "pos_y", "pos_z", "dz", "lifted", "tilt", "contact", "goal_dist", "in_goal", "used"]
PHYS = ([f"obj{i}_{n}" for i in (1, 2) for n in SLOT] + [f"art_{n}" for n in ["dist", "ddist", "contact", "true", "used"]]
        + ["grip_open", "eef_x", "eef_y", "eef_z"])
STATE = [f"obj{i}_{n}" for i in (1, 2) for n in ["dist", "pos_x", "pos_y", "pos_z", "dz", "tilt", "contact", "goal_dist"]] \
    + ["art_dist", "art_contact", "grip_open", "eef_x", "eef_y", "eef_z"]
S = [PHYS.index(n) for n in STATE]
GROUPS = {"eef": [n.startswith("eef") for n in STATE], "grip": [n == "grip_open" for n in STATE],
          "contact": [n.endswith("contact") for n in STATE]}
GROUPS["obj"] = [not (a or b or c) for a, b, c in zip(*GROUPS.values())]
CONTACT = [PHYS.index(n) for n in ["obj1_contact", "obj2_contact", "art_contact"]]
TTC_SLOTS = [("obj1_dist", "obj1_ddist"), ("obj2_dist", "obj2_ddist"), ("art_dist", "art_ddist")]
CAP = 50.0


def chunks_of(actions, q):
    return np.stack([np.pad(actions[s:s + 8], ((0, max(0, s + 8 - len(actions))), (0, 0))).reshape(-1) for s in q])


def rolling(X, w, fn):
    """fn over the last w rows at each row (fewer at the start)."""
    return np.stack([fn(X[max(0, i - w + 1):i + 1]) for i in range(len(X))])


def lag1_ac(W):
    if len(W) < 3:
        return np.zeros(W.shape[1])
    a, b = W[:-1] - W[:-1].mean(0), W[1:] - W[1:].mean(0)
    den = np.sqrt((a * a).sum(0) * (b * b).sum(0))
    return np.where(den > 1e-12, (a * b).sum(0) / np.maximum(den, 1e-12), 0.0)


def jerk(eef):
    j = np.zeros(len(eef))
    if len(eef) > 3:
        j[3:] = np.linalg.norm(np.diff(eef, n=3, axis=0), axis=1)
    return j


# ---- load ----
eps = []
for f in sorted(f for pat in args.episodes for f in glob.glob(pat)):
    ep = np.load(f, allow_pickle=True)
    if bool(ep["induced"]):
        continue
    eid = os.path.splitext(os.path.basename(f))[0]
    q = ep["query_steps"].astype(int)
    ph = np.load(os.path.join(args.phys, eid + ".npz"))["x"].astype(np.float64)
    assert len(ph) == len(q), eid
    eps.append(dict(eid=eid, q=q, phys=ph, chunks=chunks_of(ep["actions"], q), actions=ep["actions"],
                    eef=ep["eef"], feat=ep["features_mean"].astype(np.float32), success=bool(ep["success"]),
                    group=int(ep["task_id"]) if args.split == "task" else int(ep["episode_idx"]) % args.folds))
groups = sorted({e["group"] for e in eps})
print(f"{len(eps)} episodes, {sum(e['success'] for e in eps)} successes, split {args.split}, groups {groups}", flush=True)


def transitions(e):
    """Inputs (state at t-1 + chunk at t-1) and targets (change of the 22 state numbers) for t = 1 .. n-1."""
    return np.concatenate([e["phys"][:-1], e["chunks"][:-1]], 1), e["phys"][1:, S] - e["phys"][:-1, S]


names = {}
for g in groups:
    fit = [e for e in eps if e["success"] and e["group"] != g]
    Xs, Ys = zip(*[transitions(e) for e in fit])
    X, Y = np.concatenate(Xs), np.concatenate(Ys)
    xm, xs, ym, ys = X.mean(0), X.std(0) + 1e-6, Y.mean(0), Y.std(0) + 1e-6
    fm = MLPRegressor(hidden_layer_sizes=(64,), max_iter=200, early_stopping=True, random_state=args.seed).fit((X - xm) / xs, (Y - ym) / ys)
    pca = PCA(16, random_state=args.seed).fit(np.concatenate([e["feat"] for e in fit]))
    jthr = np.percentile(np.concatenate([jerk(e["eef"]) for e in fit]), 99)
    test = [e for e in eps if e["group"] == g]
    print(f"group {g}: fitted on {len(fit)} successes ({len(X)} transitions, forward R2 "
          f"{fm.score((X - xm) / xs, (Y - ym) / ys):.3f}, jerk thr {jthr:.2e}), applying to {len(test)}", flush=True)
    for e in test:
        n, ph = len(e["q"]), e["phys"]
        # 1. surprise
        err = np.zeros((n, len(S)))
        if n > 1:
            Xt, Yt = transitions(e)
            err[1:] = (fm.predict((Xt - xm) / xs).reshape(len(Xt), -1) - (Yt - ym) / ys) ** 2
        parts = [err.mean(1)] + [err[:, np.array(m)].mean(1) for m in GROUPS.values()]
        sur = np.stack(parts, 1)
        sur = np.concatenate([sur, rolling(sur, 4, lambda W: W.mean(0))], 1)
        sur_n = ["surp_total", *[f"surp_{k}" for k in GROUPS]]
        sur_n = sur_n + [f"{k}_mean4" for k in sur_n]
        # 2. critical slowing down
        sig = np.concatenate([sur[:, :1], ph[:, S], pca.transform(e["feat"])], 1)
        sig_n = ["surp_total"] + STATE + [f"pca{i}" for i in range(16)]
        csd, csd_n = [], []
        for w in (4, 8):
            csd += [rolling(sig, w, lambda W: W.var(0)), rolling(sig, w, lag1_ac)]
            csd_n += [f"{k}_var{w}" for k in sig_n] + [f"{k}_ac{w}" for k in sig_n]
        csd = np.concatenate(csd, 1)
        # 3. time-to-contact
        ttc, ttc_n = [], []
        for dn, vn in TTC_SLOTS:
            dist, closing = ph[:, PHYS.index(dn)], -ph[:, PHYS.index(vn)]
            on = closing > 1e-3
            t = np.where(on, np.minimum(dist / np.maximum(closing, 1e-3), CAP), CAP)
            ttc += [np.log1p(t), on.astype(float)]
            ttc_n += [f"{dn[:4]}_logttc", f"{dn[:4]}_closing"]
        ttc = np.stack(ttc, 1)
        # 4. micro-event rates (last 8 queries)
        flick = np.zeros(n)
        flick[1:] = np.abs(np.diff(ph[:, CONTACT], axis=0)).sum(1)
        grip = e["actions"][:, 6]
        reopen = np.zeros(len(grip))
        reopen[1:] = (grip[:-1] > 0) & (grip[1:] < 0)
        spikes = jerk(e["eef"]) > jthr
        cnt = lambda a, s: a[max(0, s - 63):s + 1].sum()  # noqa: E731
        micro = np.stack([rolling(flick[:, None], 8, lambda W: W.sum(0))[:, 0],
                          [cnt(reopen, min(s + 7, len(grip) - 1)) for s in e["q"]],  # chunk at t is known at t
                          [cnt(spikes, min(s, len(spikes) - 1)) for s in e["q"]]], 1)
        micro_n = ["contact_flicker8", "grip_reopen8", "jerk_spikes8"]
        sets = {"surprise": (sur, sur_n), "csd": (csd, csd_n), "ttc": (ttc, ttc_n), "micro": (micro, micro_n)}
        sets["bio"] = (np.concatenate([v[0] for v in sets.values()], 1), sum([v[1] for v in sets.values()], []))
        sets["bioplus"] = (np.concatenate([sets["bio"][0], ph], 1), sets["bio"][1] + PHYS)
        for k, (x, nm) in sets.items():
            os.makedirs(os.path.join(args.out, k), exist_ok=True)
            assert x.shape == (n, len(nm)) and np.isfinite(x).all(), (e["eid"], k)
            np.savez(os.path.join(args.out, k, e["eid"] + ".npz"), x=x.astype(np.float32), names=np.array(nm), query_steps=e["q"])
            names[k] = len(nm)
print(f"done: {len(eps)} episodes -> {args.out}, dims {names}")
