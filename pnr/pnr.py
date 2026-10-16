"""Point-of-no-return (PNR) maths. Pure numpy, no simulator needed, so it is easy to test."""

from __future__ import annotations

from typing import Optional, Sequence

import numpy as np


def value_curve(successes: np.ndarray) -> np.ndarray:
    """successes: [num_checkpoints, K] array of 0/1. Returns value(t) = mean success per checkpoint."""
    successes = np.asarray(successes, dtype=float)
    return successes.mean(axis=1)


def find_pnr(checkpoints: Sequence[int], successes: np.ndarray, min_fail: int) -> Optional[int]:
    """First checkpoint with at least `min_fail` failed replays such that every later
    checkpoint also has at least `min_fail` failures. Returns None if there is no such checkpoint.

    checkpoints: policy-step indices, increasing.
    successes:   [len(checkpoints), K] array of 0/1 replay outcomes.
    """
    successes = np.asarray(successes, dtype=int)
    k = successes.shape[1]
    fails = k - successes.sum(axis=1)
    bad = fails >= min_fail
    # Walk backwards: find the start of the final run of "bad" checkpoints.
    if len(bad) == 0 or not bad[-1]:
        return None
    i = len(bad) - 1
    while i > 0 and bad[i - 1]:
        i -= 1
    return int(checkpoints[i])


def timeline_row(t_pnr: Optional[int], t_alarm: Optional[int], t_onset: Optional[int]) -> dict:
    """Detection window = t_alarm - t_pnr, intervention window = t_onset - t_pnr (lab terms, Oct 2 2026)."""
    def diff(a, b):
        return None if a is None or b is None else int(a) - int(b)

    return {
        "t_pnr": t_pnr,
        "t_alarm": t_alarm,
        "t_onset": t_onset,
        "detection_window": diff(t_alarm, t_pnr),
        "intervention_window": diff(t_onset, t_pnr),
    }


def value_at(checkpoints: Sequence[int], successes: np.ndarray, t: Optional[int]) -> Optional[float]:
    """Replay value at the last scanned checkpoint at or before step t (None if not scanned)."""
    if t is None:
        return None
    vals = value_curve(successes)
    best = None
    for c, v in zip(checkpoints, vals):
        if c <= t:
            best = float(v)
    return best


def classify_alarm(t_alarm: Optional[int], t_pnr: Optional[int], t_onset: Optional[int],
                   value: Optional[float], episode_succeeded: bool) -> Optional[str]:
    """Seongheon's framing: an alarm is only useful if it lets someone intervene while it still matters,
    without stopping a robot that would recover by itself.
      unnecessary_stop: alarm on an episode that succeeded anyway
      early:            alarm before PNR, or where replays mostly still succeed (value >= 0.5)
      late:             alarm after the human could already see the failure (t_onset)
      in_window:        after PNR and before onset (the useful case)
    """
    if t_alarm is None:
        return None
    if episode_succeeded:
        return "unnecessary_stop"
    if (t_pnr is not None and t_alarm < t_pnr) or (value is not None and value >= 0.5):
        return "early"
    if t_onset is not None and t_alarm > t_onset:
        return "late"
    return "in_window"
