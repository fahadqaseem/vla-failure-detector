from __future__ import annotations

import numpy as np

from .data import Trajectory
from .signals import compute_action_signals


def stac_scores(
    trajectories: list[Trajectory],
    execution_horizon: int,
    beta: float,
) -> dict[str, np.ndarray]:
    raw = {
        trajectory.key: compute_action_signals(
            trajectory.action_chunks, execution_horizon, beta
        ).consistency
        for trajectory in trajectories
    }
    flat = np.concatenate(list(raw.values()))
    low, high = np.percentile(flat, [1.0, 99.0])
    return {
        key: np.clip((value - low) / (high - low + 1e-8), 0.0, 1.0).astype(np.float32)
        for key, value in raw.items()
    }
