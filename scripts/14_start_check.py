"""Start-of-run check (Fahad, Oct 22): from the first query alone, predict "doomed from step 0" (t_pnr 0) vs not.

Inputs = the step-0 row of the predictor: features_mean at the first query (4096) + its action chunk (8 x 7) + eef
position (3) + gripper qpos (2). Episodes and labels = the held-out rows of a 06_train_predictor.py run
(per_episode.json, one row per episode): positive = doomed from start, negative = every other episode (successes,
recoverable failures, failures with t_pnr > 0). Leave-one-task-out.
Models: logreg (one linear layer) and mlp (256, ReLU), BCE with positives and negatives weighted equally, Adam,
full batch, standardised on the training rows; same settings as 06_train_predictor.py.
Threshold: conformal at --alpha on the scores of all training-task successes, cross-fitted (each from a model that did
not see that task), as in 06. Caught = doomed runs of the held-out task above it; false alarms on its successes.

python scripts/14_start_check.py --pred results/predictor_with_perturbed --out results/lead_experiments/start_check
"""

import argparse
import glob
import json
import os

import numpy as np
import torch
from sklearn.metrics import roc_auc_score

p = argparse.ArgumentParser()
p.add_argument("--pred", default="results/predictor_with_perturbed", help="per_episode.json with the labelled episodes")
p.add_argument("--episodes", nargs="+", default=["data/natural/*/*.npz", "data/perturbed/task0[0145678]/*.npz"])
p.add_argument("--alpha", type=float, default=0.05)
p.add_argument("--epochs", type=int, default=300)
p.add_argument("--lr", type=float, default=1e-3)
p.add_argument("--weight_decay", type=float, default=1e-3)
p.add_argument("--hidden", type=int, default=256)
p.add_argument("--seed", type=int, default=0)
p.add_argument("--out", default="results/lead_experiments/start_check")
args = p.parse_args()

rows = {r["eid"]: r for r in json.load(open(os.path.join(args.pred, "per_episode.json")))}  # one row per episode
files = {os.path.splitext(os.path.basename(f))[0]: f for pat in args.episodes for f in glob.glob(pat)}
eps = []
for eid, r in sorted(rows.items()):
    ep = np.load(files[eid], allow_pickle=True)
    x = np.concatenate([ep["features_mean"][0].astype(np.float32), ep["actions"][:8].reshape(-1),
                        ep["eef"][int(ep["query_steps"][0])], ep["query_grippers"][0]]).astype(np.float32)
    eps.append(dict(eid=eid, task=r["task"], success=r["success"], doomed=r["t_pnr"] == 0, x=x,
                    source="perturbed" if eid.endswith("_p0") else "natural"))
print(f"{len(eps)} episodes, {sum(e['doomed'] for e in eps)} doomed, {sum(e['success'] for e in eps)} successes", flush=True)


def train(train_eps, model_name):
    torch.manual_seed(args.seed)
    X = np.stack([e["x"] for e in train_eps])
    y = np.array([e["doomed"] for e in train_eps], np.float32)
    mu, sd = X.mean(0), X.std(0) + 1e-6
    w = np.where(y == 1, 0.5 / max(y.sum(), 1), 0.5 / max((1 - y).sum(), 1)).astype(np.float32)
    d = X.shape[1]
    net = (torch.nn.Linear(d, 1) if model_name == "logreg" else
           torch.nn.Sequential(torch.nn.Linear(d, args.hidden), torch.nn.ReLU(), torch.nn.Linear(args.hidden, 1)))
    opt = torch.optim.Adam(net.parameters(), lr=args.lr, weight_decay=args.weight_decay)
    Xt, yt, wt = torch.tensor((X - mu) / sd), torch.tensor(y), torch.tensor(w)
    for _ in range(args.epochs):
        loss = (torch.nn.functional.binary_cross_entropy_with_logits(net(Xt).squeeze(1), yt, reduction="none") * wt).sum()
        opt.zero_grad()
        loss.backward()
        opt.step()
    net.eval()
    return lambda es: torch.sigmoid(net(torch.tensor((np.stack([e["x"] for e in es]) - mu) / sd)).squeeze(1)).detach().numpy()


def conformal_threshold(scores, alpha):
    n = len(scores)
    k = int(np.ceil((n + 1) * (1 - alpha)))
    return np.inf if k > n else float(np.sort(scores)[k - 1])


tasks = sorted({e["task"] for e in eps})
lines = [f"# Start-of-run check: doomed from step 0, from the first query only, leave-one-task-out ({args.pred})", "",
         "Natural and perturbed-natural (7 of 10 tasks) pooled. Threshold: conformal "
         f"{args.alpha:.0%} on cross-fitted training-task successes.", "",
         "| model | AUROC doomed vs rest | AUROC doomed vs successes | doomed caught | natural / perturbed caught "
         "| false alarms on successes | alarms on other failures |", "|---|---|---|---|---|---|---|"]
per_ep = []
for m in ["logreg", "mlp"]:
    out = []  # (episode, score, alarm)
    for t in tasks:
        tr = [e for e in eps if e["task"] != t]
        calib = []
        for u in sorted({e["task"] for e in tr}):
            score_u = train([e for e in tr if e["task"] != u], m)
            calib += list(score_u([e for e in tr if e["task"] == u and e["success"]]))
        thr = conformal_threshold(np.array(calib), args.alpha)
        te = [e for e in eps if e["task"] == t]
        out += [(e, float(s), bool(s > thr)) for e, s in zip(te, train(tr, m)(te))]
        print(f"{m} held-out task {t}: threshold {thr:.3f}", flush=True)
    y = np.array([e["doomed"] for e, _, _ in out])
    s = np.array([sc for _, sc, _ in out])
    succ = np.array([e["success"] for e, _, _ in out])
    a = np.array([al for _, _, al in out])
    other_fail = ~y & ~succ
    caught = {src: sum(al for e, _, al in out if e["doomed"] and e["source"] == src) for src in ["natural", "perturbed"]}
    n_doomed = {src: sum(e["doomed"] and e["source"] == src for e, _, _ in out) for src in ["natural", "perturbed"]}
    lines.append(f"| {m} | {roc_auc_score(y, s):.3f} | {roc_auc_score(y[y | succ], s[y | succ]):.3f} | "
                 f"{int(a[y].sum())} of {int(y.sum())} | {caught['natural']} of {n_doomed['natural']} / "
                 f"{caught['perturbed']} of {n_doomed['perturbed']} | {int(a[succ].sum())} of {int(succ.sum())} "
                 f"({a[succ].mean():.3f}) | {int(a[other_fail].sum())} of {int(other_fail.sum())} |")
    per_ep += [dict(model=m, eid=e["eid"], task=e["task"], success=e["success"], doomed=e["doomed"], score=sc, alarm=al)
               for e, sc, al in out]
os.makedirs(args.out, exist_ok=True)
text = "\n".join(lines) + "\n"
open(os.path.join(args.out, "summary.md"), "w").write(text)
json.dump(per_ep, open(os.path.join(args.out, "per_episode.json"), "w"), indent=1)
print(text)
