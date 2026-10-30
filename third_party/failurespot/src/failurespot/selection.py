from __future__ import annotations

import numpy as np

from .data import Trajectory


def binary_entropy(probabilities: np.ndarray) -> np.ndarray:
    probabilities = np.clip(np.asarray(probabilities, dtype=np.float64), 1e-8, 1 - 1e-8)
    return -(
        probabilities * np.log(probabilities)
        + (1.0 - probabilities) * np.log(1.0 - probabilities)
    )


def trajectory_uncertainty(probabilities: np.ndarray) -> float:
    """Return mean entropy across every timestamp."""

    values = np.asarray(probabilities)
    if values.ndim != 1 or len(values) == 0:
        raise ValueError("Expected a non-empty timestamp probability sequence")
    return float(binary_entropy(values).mean())


def select_by_uncertainty(
    trajectories: list[Trajectory],
    scores: dict[str, np.ndarray],
    budget: int,
) -> list[Trajectory]:
    if not 0 <= budget <= len(trajectories):
        raise ValueError("budget must be between zero and the candidate count")
    ranked = sorted(
        trajectories,
        key=lambda trajectory: (
            -trajectory_uncertainty(scores[trajectory.key]),
            trajectory.task_id,
            trajectory.episode_id,
        ),
    )
    return ranked[:budget]


def select_random(
    trajectories: list[Trajectory],
    budget: int,
    seed: int,
) -> list[Trajectory]:
    if not 0 <= budget <= len(trajectories):
        raise ValueError("budget must be between zero and the candidate count")
    rng = np.random.default_rng(seed)
    indices = rng.choice(len(trajectories), size=budget, replace=False)
    return [trajectories[int(index)] for index in indices]
