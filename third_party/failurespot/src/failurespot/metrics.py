from __future__ import annotations

import numpy as np

from .data import Trajectory


def binary_auroc(labels, scores) -> float:
    labels = np.asarray(labels, dtype=np.int64)
    scores = np.asarray(scores, dtype=np.float64)
    positives = int((labels == 1).sum())
    negatives = int((labels == 0).sum())
    if positives == 0 or negatives == 0:
        return float("nan")
    order = np.argsort(scores, kind="mergesort")
    ranks = np.empty(len(scores), dtype=np.float64)
    start = 0
    while start < len(scores):
        end = start + 1
        while end < len(scores) and scores[order[end]] == scores[order[start]]:
            end += 1
        ranks[order[start:end]] = 0.5 * (start + 1 + end)
        start = end
    positive_rank_sum = ranks[labels == 1].sum()
    return float(
        (positive_rank_sum - positives * (positives + 1) / 2)
        / (positives * negatives)
    )


def balanced_accuracy(labels, predictions) -> float:
    labels = np.asarray(labels, dtype=np.int64)
    predictions = np.asarray(predictions, dtype=np.int64)
    positive = labels == 1
    negative = labels == 0
    if not positive.any() or not negative.any():
        return float("nan")
    true_positive_rate = float((predictions[positive] == 1).mean())
    true_negative_rate = float((predictions[negative] == 0).mean())
    return 0.5 * (true_positive_rate + true_negative_rate)


def evaluate_scores(
    trajectories: list[Trajectory],
    scores: dict[str, np.ndarray],
) -> dict[str, float]:
    timestamp_labels = np.concatenate(
        [trajectory.timestamp_labels for trajectory in trajectories]
    )
    timestamp_scores = np.concatenate([scores[trajectory.key] for trajectory in trajectories])
    trajectory_labels = np.asarray(
        [trajectory.trajectory_label for trajectory in trajectories], dtype=np.int64
    )
    trajectory_scores = np.asarray(
        [float(np.max(scores[trajectory.key])) for trajectory in trajectories]
    )
    return {
        "timestamp_auroc": binary_auroc(timestamp_labels, timestamp_scores),
        "trajectory_auroc": binary_auroc(trajectory_labels, trajectory_scores),
        "trajectory_count": len(trajectories),
        "timestamp_count": int(len(timestamp_labels)),
    }
