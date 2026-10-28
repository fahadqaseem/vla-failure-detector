"""Per-query features from the dense open-loop replays (pnr_probe, Oct 28 2026). Episodes whose replay failed the
fidelity check (eef drift > 10 mm at a checkpoint, dense_replay.py) are left out everywhere.

Dense features at query k use only the steps executed before it (steps < q_k); 0 at the first query:
  micro (last 64 steps = 8 queries)
    contact_flicker   on/off changes of finger pad contact (normal force > 0), both pads summed
    force_spikes      steps whose pad force change (both pads summed, N) is above the 99th percentile of fitting successes
    grip_slip         steps where the gripper is commanded closed, both pads held > 1 N the step before and not now
  torque disturbance  expected joint torque = MLP 64 (scikit-learn) from qpos, qvel and the action at the same step to
                      qfrc_actuator (9 robot dofs), fitted on successes; disturbance = squared error in standardised units,
                      mean over dofs; per query: mean and max over the last 8 steps, mean over the last 32 steps
  force surprise      forward model = MLP 64 from qpos, qvel, action, pad forces and qfrc_constraint at step t - 1 to pad forces
                      and qfrc_constraint at t, fitted on successes; error as above; same 3 aggregates
Anything fitted (models, spike threshold) uses only successes outside the episode's group: other tasks (--split task,
leave-one-task-out) or other folds episode_idx % 5 (--split episode, seen), as in 06_train_predictor.py. "Expected
torque per task" is therefore a model of torque given the robot state and action, learned on the other tasks.

Outputs (same format as 20_physical_signals.py, read by 06 with --phys):
  --out/a/<eid>.npz   Track 1 physical (33) + old micro-events (3, pnr_probe/data/<split>/micro)
  --out/b/<eid>.npz   a + dense (9)
  --out/passed.txt    episode files that passed the replay check (the episode list of every dense run)

python pnr_probe/dense/dense_features.py --split task --micro pnr_probe/data/unseen/micro --out pnr_probe/data/dense_feat/unseen
"""

import argparse
import glob
import os

import numpy as np
from sklearn.neural_network import MLPRegressor

D = os.path.expanduser("~/vla-failure-detector/data")
p = argparse.ArgumentParser()
p.add_argument("--episodes", nargs="+", default=[f"{D}/natural/*/*.npz", f"{D}/perturbed/task0[0145678]/*.npz",
                                                  f"{D}/perturbed_v2/task0[0147]/*.npz"])
p.add_argument("--dense", default="pnr_probe/data/dense")
p.add_argument("--phys", default=f"{D}/physical")
p.add_argument("--micro", required=True)
p.add_argument("--split", choices=["task", "episode"], default="task")
p.add_argument("--folds", type=int, default=5)
p.add_argument("--max_rows", type=int, default=150000, help="steps sampled to fit each regressor")
p.add_argument("--out", required=True)
p.add_argument("--seed", type=int, default=0)
args = p.parse_args()

W, HOLD = 64, 1.0
NAMES = ["contact_flicker64", "force_spikes64", "grip_slip64", "torque_dist_mean8", "torque_dist_max8", "torque_dist_mean32",
         "force_surp_mean8", "force_surp_max8", "force_surp_mean32"]

eps, missing, failed = [], [], []
for f in sorted(f for pat in args.episodes for f in glob.glob(pat)):
    ep = np.load(f, allow_pickle=True)
    if bool(ep["induced"]):
        continue
    eid = os.path.splitext(os.path.basename(f))[0]
    dp = os.path.join(args.dense, eid + ".npz")
    if not os.path.exists(dp):
        missing.append(eid)
        continue
    dz = np.load(dp)
    if not bool(dz["passed"]):
        failed.append(eid)
        continue
    a = ep["actions"]
    step_in = np.concatenate([dz["qpos"], dz["qvel"], a], 1)                              # torque model input at t
    fsig = np.concatenate([dz["finger_force"], dz["qfrc_constraint"]], 1)                  # force state
    eps.append(dict(eid=eid, file=f, q=ep["query_steps"].astype(int), success=bool(ep["success"]),
                    group=int(ep["task_id"]) if args.split == "task" else int(ep["episode_idx"]) % args.folds,
                    step_in=step_in, tau=dz["qfrc_actuator"].astype(np.float64), fsig=fsig.astype(np.float64),
                    ff=dz["finger_force"].astype(np.float64), grip=a[:, 6]))
print(f"{len(eps)} episodes passed, {len(failed)} failed replay, {len(missing)} without dense replay", flush=True)
assert not missing, missing[:5]
os.makedirs(args.out, exist_ok=True)
open(os.path.join(args.out, "passed.txt"), "w").write("\n".join(e["file"] for e in eps) + "\n")
open(os.path.join(args.out, "failed_replay.txt"), "w").write("\n".join(failed) + "\n")


def fit(X, Y, rng):
    if len(X) > args.max_rows:
        i = rng.choice(len(X), args.max_rows, replace=False)
        X, Y = X[i], Y[i]
    xm, xs, ym, ys = X.mean(0), X.std(0) + 1e-6, Y.mean(0), Y.std(0) + 1e-6
    m = MLPRegressor(hidden_layer_sizes=(64,), max_iter=100, early_stopping=True, random_state=args.seed).fit((X - xm) / xs, (Y - ym) / ys)
    r2 = m.score((X - xm) / xs, (Y - ym) / ys)
    predict = lambda Xn: m.predict((Xn - xm) / xs).reshape(len(Xn), -1)  # noqa: E731  (standardised units)
    return predict, (ym, ys), r2


def per_query(err, q, n):
    """Aggregates of a per-step error over the steps before each query."""
    out = np.zeros((len(q), n))
    for k, s in enumerate(q):
        if s == 0:
            continue
        out[k] = [err[max(0, s - 8):s].mean(), err[max(0, s - 8):s].max(), err[max(0, s - 32):s].mean()]
    return out


def window_count(ev, q):
    c = np.concatenate([[0], np.cumsum(ev)])
    return np.array([c[s] - c[max(0, s - W)] for s in q], np.float64)


rng = np.random.default_rng(args.seed)
for g in sorted({e["group"] for e in eps}):
    fitset = [e for e in eps if e["success"] and e["group"] != g]
    tq_pred, (tm, ts), r2t = fit(np.concatenate([e["step_in"] for e in fitset]), np.concatenate([e["tau"] for e in fitset]), rng)
    fx = np.concatenate([np.concatenate([e["step_in"][:-1], e["fsig"][:-1]], 1) for e in fitset])
    fy = np.concatenate([e["fsig"][1:] for e in fitset])
    fs_pred, (fm, fsd), r2f = fit(fx, fy, rng)
    jump = lambda e: np.abs(np.diff(e["ff"].sum(1), prepend=e["ff"][:1].sum(1)))  # noqa: E731
    thr = np.percentile(np.concatenate([jump(e) for e in fitset]), 99)
    test = [e for e in eps if e["group"] == g]
    print(f"group {g}: {len(fitset)} fitting successes, torque R2 {r2t:.3f}, force R2 {r2f:.3f}, spike thr {thr:.2f} N, "
          f"{len(test)} episodes", flush=True)
    for e in test:
        q, n = e["q"], len(e["q"])
        contact = e["ff"] > 0
        flick = np.zeros(len(contact))
        flick[1:] = (contact[1:] != contact[:-1]).sum(1)
        held = (e["ff"] > HOLD).all(1)
        slip = np.zeros(len(held))
        slip[1:] = held[:-1] & ~held[1:] & (e["grip"][1:] > 0)
        micro = np.stack([window_count(flick, q), window_count(jump(e) > thr, q), window_count(slip, q)], 1)
        tdist = (((tq_pred(e["step_in"]) - (e["tau"] - tm) / ts)) ** 2).mean(1)
        fsur = np.zeros(len(e["ff"]))
        if len(fsur) > 1:
            fsur[1:] = ((fs_pred(np.concatenate([e["step_in"][:-1], e["fsig"][:-1]], 1)) - (e["fsig"][1:] - fm) / fsd) ** 2).mean(1)
        dense = np.concatenate([micro, per_query(tdist, q, 3), per_query(fsur, q, 3)], 1)
        ph = np.load(os.path.join(args.phys, e["eid"] + ".npz"))
        mi = np.load(os.path.join(args.micro, e["eid"] + ".npz"))
        a = np.concatenate([ph["x"], mi["x"]], 1)
        names_a = list(ph["names"]) + list(mi["names"])
        for k, (x, nm) in {"a": (a, names_a), "b": (np.concatenate([a, dense], 1), names_a + NAMES)}.items():
            os.makedirs(os.path.join(args.out, k), exist_ok=True)
            assert x.shape == (n, len(nm)) and np.isfinite(x).all(), (e["eid"], k)
            np.savez(os.path.join(args.out, k, e["eid"] + ".npz"), x=x.astype(np.float32), names=np.array(nm), query_steps=q)
print(f"done -> {args.out}")
