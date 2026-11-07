"""Shared loading for the Nov 7 audit analyses (results/plan_nov06.md, "Nov 7 additions"). Unseen tasks (leave one task out) only.

Score sources (per policy, rule thr in 50 / 70 / 80):
  progress, gru_phys_ttp seed 0    data/week3_reg (OpenVLA-OFT), data/pi05_reg (Pi0.5): thr{T}/unseen/all_scores.json
  gru_phys_ttp seeds 1 to 4        data/seeds/{pol}/thr{T}/unseen/s{S}/gru_phys_ttp/all_scores.json
  gru_phys_ttp_ens, or_progress_ens   data/ens/{pol}/thr{T}/merged (50_ensemble.py)
  or_progress_ttp seed S           data/combo/{pol}/thr{T}/merged (seed 0), data/combo_seeds/{pol}/thr{T}/s{S}/merged (alarms only)
"""

import functools
import json
import os

import numpy as np

POLS = {"oft": "OpenVLA-OFT", "pi05": "Pi0.5"}
REG = {"oft": "data/week3_reg", "pi05": "data/pi05_reg"}
RULES = {50: "50%", 70: "70% (main)", 80: "80%"}
KEYS = ["fixed 0.025", "fixed 0.05"]
DROP = ("labels", "scores", "steps", "risk", "ttp")


@functools.lru_cache(maxsize=8)
def _json(path):
    return json.load(open(path))


def scores(pol, thr, model, seed=0):
    """Rows with per-step scores (progress, gru_phys*, gru_phys_ttp seeds, gru_phys_ttp_ens)."""
    if model == "gru_phys_ttp_ens":
        path = f"data/ens/{pol}/thr{thr}/merged/all_scores.json"
    elif seed == 0 or model == "progress":
        path = os.path.join(REG[pol], f"thr{thr}", "unseen", "all_scores.json")
    else:
        path = f"data/seeds/{pol}/thr{thr}/unseen/s{seed}/{model}/all_scores.json"
    return [r for r in _json(path) if r["model"] == model]


def alarms(pol, thr, model, seed=0):
    """Rows with alarms only (every model, including the OR rules)."""
    if model == "or_progress_ttp":
        d = f"data/combo/{pol}/thr{thr}/merged" if seed == 0 else f"data/combo_seeds/{pol}/thr{thr}/s{seed}/merged"
        return [r for r in _json(os.path.join(d, "per_episode.json")) if r["model"] == model]
    if model == "or_progress_ens":
        return [r for r in _json(f"data/ens/{pol}/thr{thr}/merged/per_episode.json") if r["model"] == model]
    return scores(pol, thr, model, seed)


def main_models(have_or_seeds=True):
    """(label, model, seed) of the audit: progress, gru_phys_ttp seeds 0 to 4, the ensemble, and the OR rules."""
    out = [("progress", "progress", 0)] + [(f"gru_phys_ttp s{s}", "gru_phys_ttp", s) for s in range(5)]
    out += [("gru_phys_ttp_ens", "gru_phys_ttp_ens", 0)]
    out += [(f"or_progress_ttp s{s}", "or_progress_ttp", s) for s in (range(5) if have_or_seeds else [0])]
    out += [("or_progress_ens", "or_progress_ens", 0)]
    return out


def timed(r):
    return not r["success"] and r["t_pnr"] not in (None, 0)


def recoverable(r):
    return not r["success"] and r["t_pnr"] is None


def caught(r, key):
    a = r["alarms"][key]
    return a is not None and a <= r["t_pnr"]


def first_alarm(r, thr):
    above = np.nonzero(np.asarray(r["scores"], float) > thr)[0]
    return r["steps"][above[0]] if len(above) else None


def threshold_at(succ_max, rate):
    """Lowest threshold with at most `rate` of the given successes above it (descriptive sweeps on held-out successes)."""
    for t in np.unique(np.r_[succ_max, np.inf]):
        if np.mean(succ_max > t) <= rate + 1e-12:
            return t
    return np.inf


def conformal_threshold(run_maxes, alpha):  # same as 06_train_predictor.py
    n = len(run_maxes)
    k = int(np.ceil((n + 1) * (1 - alpha)))
    return np.inf if k > n else float(np.sort(run_maxes)[k - 1])
