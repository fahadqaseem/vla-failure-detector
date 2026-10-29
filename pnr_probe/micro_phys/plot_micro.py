"""pnr_probe copy of scripts/21_plot_physical.py (Oct 29 2026) for the 3 micro-event counts (pnr_probe/data/unseen/micro):
only the figure grid (1 x 3) and the data wording changed. All data: natural + perturbed + perturbed_v2, pooled.

Visual check of the physical signals around t_pnr (Track 1, Oct 23 2026).

Failures: every labelled failure with t_pnr > 0 of --pred (46: natural + perturbed, 7 of 10 tasks, pooled). Matched
successes: for each failure, one success of the same task and the same source (natural / perturbed), the lowest
initial-state index not used yet. Both are read at the SAME absolute steps, t_pnr - 200 to t_pnr + 100 (relative step
r = step - t_pnr of the failure), so time is matched; a success that already ended has no value there.
Per signal: median and 25 to 75% band per relative step, failures vs matched successes (one png per signal and one
overview). Summary: per signal, AUROC failures vs matched successes of the per-episode mean in three windows
(early -200 to -136, just before -64 to 0, just after 0 to +64; 0.5 = no difference), with the number of episodes.

python scripts/21_plot_physical.py --phys data/physical --out results/week2/physical_signals
"""

import argparse
import glob
import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from sklearn.metrics import roc_auc_score  # noqa: E402

p = argparse.ArgumentParser()
p.add_argument("--phys", default="data/physical")
p.add_argument("--pred", default="results/predictor_with_perturbed")
p.add_argument("--out", default="results/week2/physical_signals")
p.add_argument("--before", type=int, default=200)
p.add_argument("--after", type=int, default=100)
args = p.parse_args()

rows = [r for r in json.load(open(os.path.join(args.pred, "per_episode.json"))) if r["model"] == "progress"]
source = lambda eid: "perturbed" if "_p" in eid else "natural"  # noqa: E731
idx = lambda eid: int(eid.split("_")[1][1:])  # noqa: E731
fails = sorted((r for r in rows if not r["success"] and r["t_pnr"] not in (None, 0)), key=lambda r: r["eid"])
used, pairs = set(), []
for r in fails:
    cands = sorted((s for s in rows if s["success"] and s["task"] == r["task"] and source(s["eid"]) == source(r["eid"])
                    and s["eid"] not in used), key=lambda s: idx(s["eid"]))
    if cands:
        used.add(cands[0]["eid"])
    pairs.append((r, cands[0] if cands else None))
phys = {os.path.splitext(os.path.basename(f))[0]: np.load(f) for f in glob.glob(os.path.join(args.phys, "*.npz"))}
names = [str(n) for n in next(iter(phys.values()))["names"]]
show = [i for i, n in enumerate(names) if not n.endswith("_used")]
rel = np.arange(-args.before, args.after + 1, 8)


def aligned(eid, t_pnr):
    """(len(rel), n_signals), nan where the episode has no query at that step."""
    d = phys[eid]
    at = {int(s): k for k, s in enumerate(d["query_steps"])}
    out = np.full((len(rel), len(names)), np.nan)
    for j, r in enumerate(rel):
        k = at.get(int(t_pnr + r))
        if k is not None:
            out[j] = d["x"][k]
    return out


F = np.stack([aligned(r["eid"], r["t_pnr"]) for r, _ in pairs])
S = np.stack([aligned(s["eid"], r["t_pnr"]) if s else np.full((len(rel), len(names)), np.nan) for r, s in pairs])
os.makedirs(args.out, exist_ok=True)
WINDOWS = {"early (-200 to -136)": (-200, -136), "before (-64 to 0)": (-64, 0), "after (0 to +64)": (0, 64)}


def band(ax, A, i, color, label):
    v = A[:, :, i]
    ok = (~np.isnan(v)).sum(0) >= 3
    q = np.full((3, len(rel)), np.nan)
    q[:, ok] = np.nanpercentile(v[:, ok], [25, 50, 75], axis=0)
    ax.plot(rel, q[1], color=color, label=f"{label} (n {int((~np.isnan(v)).any(1).sum())})")
    ax.fill_between(rel, q[0], q[2], color=color, alpha=0.2)


fig, axes = plt.subplots(1, 3, figsize=(16, 4.5))
for a, i in zip(axes.ravel(), show):
    for ax in (a, plt.figure(figsize=(5, 3.5)).gca()):
        band(ax, F, i, "tab:red", "failures")
        band(ax, S, i, "tab:blue", "matched successes")
        ax.axvline(0, color="k", lw=0.8)
        ax.set_title(names[i], fontsize=9)
        ax.set_xlabel("steps from t_pnr", fontsize=8)
        if ax is not a:
            ax.legend(fontsize=7)
            ax.figure.tight_layout()
            ax.figure.savefig(os.path.join(args.out, f"{names[i]}.png"), dpi=110)
            plt.close(ax.figure)
for a in axes.ravel()[len(show):]:
    a.axis("off")
axes.ravel()[0].legend(fontsize=7)
fig.suptitle("Micro-event counts (last 8 queries) aligned to t_pnr: median and 25-75% band (all data, pooled)")
fig.tight_layout()
fig.savefig(os.path.join(args.out, "overview.png"), dpi=110)

lines = ["# Micro-event counts around t_pnr: failures vs matched successes", "",
         f"{len(fails)} failures with t_pnr > 0 (natural + perturbed + perturbed_v2, pooled), "
         f"{sum(s is not None for _, s in pairs)} matched successes (same task and source, read at the same steps). "
         "AUROC of the per-episode mean in each window, failures = positive (above 0.5 = higher in failures); "
         "n = failures / successes with data in the window.", "",
         "| signal | " + " | ".join(WINDOWS) + " |", "|---|" + "---|" * len(WINDOWS)]
summary = []
for i in show:
    cells, before = [], np.nan
    for w, (a, b) in WINDOWS.items():
        cols = (rel >= a) & (rel <= b)
        with np.errstate(all="ignore"):
            f, s = np.nanmean(F[:, cols, i], 1), np.nanmean(S[:, cols, i], 1)
        f, s = f[~np.isnan(f)], s[~np.isnan(s)]
        auc = roc_auc_score(np.r_[np.ones(len(f)), np.zeros(len(s))], np.r_[f, s]) if len(f) and len(s) and np.ptp(np.r_[f, s]) > 0 else np.nan
        cells.append(f"{auc:.2f} (n {len(f)} / {len(s)})")
        if w.startswith("before"):
            before = auc
    summary.append((abs(before - 0.5) if not np.isnan(before) else -1, f"| {names[i]} | " + " | ".join(cells) + " |"))
lines += [row for _, row in sorted(summary, reverse=True)]
lines += ["", "Rows sorted by how far the 'before' AUROC is from 0.5. Figures: overview.png and one png per signal."]
open(os.path.join(args.out, "summary.md"), "w").write("\n".join(lines) + "\n")
print("\n".join(lines))
