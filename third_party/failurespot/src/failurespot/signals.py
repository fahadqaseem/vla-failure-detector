from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .config import SignalConfig
from .data import Trajectory


@dataclass(frozen=True)
class ActionSignals:
    consistency: np.ndarray
    full_magnitude: np.ndarray
    executed_magnitude: np.ndarray
    consistency_ema: np.ndarray
    full_magnitude_ema: np.ndarray
    executed_magnitude_ema: np.ndarray


def exponential_moving_average(values: np.ndarray, beta: float = 0.8) -> np.ndarray:
    values = np.asarray(values, dtype=np.float32)
    if values.ndim != 1 or len(values) == 0:
        raise ValueError("EMA expects a non-empty one-dimensional array")
    result = np.empty_like(values)
    result[0] = values[0]
    for index in range(1, len(values)):
        result[index] = beta * result[index - 1] + (1.0 - beta) * values[index]
    return result


def compute_action_signals(
    action_chunks: np.ndarray,
    execution_horizon: int,
    beta: float = 0.8,
) -> ActionSignals:
    chunks = np.asarray(action_chunks, dtype=np.float32)
    if chunks.ndim != 3:
        raise ValueError("action_chunks must have shape [T,H,D]")
    timestamps, horizon, _ = chunks.shape
    if not 1 <= execution_horizon <= horizon:
        raise ValueError("execution_horizon must be in [1,H]")
    full = np.linalg.norm(chunks, axis=-1).mean(axis=1)
    executed = np.linalg.norm(chunks[:, :execution_horizon], axis=-1).mean(axis=1)
    consistency = np.zeros(timestamps, dtype=np.float32)
    if horizon == execution_horizon == 1:
        if timestamps > 1:
            consistency[1:] = np.linalg.norm(chunks[1:, 0] - chunks[:-1, 0], axis=-1)
    else:
        overlap = min(execution_horizon, horizon - execution_horizon)
        if overlap < 1:
            raise ValueError("Chunked policies require H>K for overlap consistency")
        for timestamp in range(1, timestamps):
            previous = chunks[timestamp - 1, execution_horizon:execution_horizon + overlap]
            current = chunks[timestamp, :overlap]
            consistency[timestamp] = np.linalg.norm(previous - current, axis=-1).mean()
    return ActionSignals(
        consistency=consistency,
        full_magnitude=full.astype(np.float32),
        executed_magnitude=executed.astype(np.float32),
        consistency_ema=exponential_moving_average(consistency, beta),
        full_magnitude_ema=exponential_moving_average(full, beta),
        executed_magnitude_ema=exponential_moving_average(executed, beta),
    )


def combined_signal(signals: ActionSignals, config: SignalConfig) -> np.ndarray:
    score = (
        config.consistency_weight * (signals.consistency + signals.consistency_ema)
        + config.full_magnitude_weight
        * (signals.full_magnitude + signals.full_magnitude_ema)
        + config.executed_magnitude_weight
        * (signals.executed_magnitude + signals.executed_magnitude_ema)
    )
    return np.asarray(score, dtype=np.float32)


@dataclass
class ActionSignalNormalizer:
    low: float
    high: float

    @classmethod
    def fit(
        cls,
        trajectories: list[Trajectory],
        execution_horizon: int,
        config: SignalConfig,
    ) -> "ActionSignalNormalizer":
        scores = [
            combined_signal(
                compute_action_signals(
                    trajectory.action_chunks, execution_horizon, config.ema_beta
                ),
                config,
            )
            for trajectory in trajectories
        ]
        flat = np.concatenate(scores)
        low, high = np.percentile(
            flat, [config.lower_percentile, config.upper_percentile]
        )
        if high <= low:
            high = low + 1.0
        return cls(float(low), float(high))

    def transform(self, values: np.ndarray) -> np.ndarray:
        return np.clip(
            (np.asarray(values, dtype=np.float32) - self.low)
            / (self.high - self.low + 1e-8),
            0.0,
            1.0,
        ).astype(np.float32)

    def labels_for(
        self,
        trajectory: Trajectory,
        execution_horizon: int,
        config: SignalConfig,
    ) -> np.ndarray:
        signals = compute_action_signals(
            trajectory.action_chunks, execution_horizon, config.ema_beta
        )
        return self.transform(combined_signal(signals, config))


def action_probe_features(
    trajectory: Trajectory,
    execution_horizon: int,
    beta: float,
) -> np.ndarray:
    signals = compute_action_signals(trajectory.action_chunks, execution_horizon, beta)
    return np.stack(
        [
            signals.consistency,
            signals.consistency_ema,
            signals.full_magnitude,
            signals.full_magnitude_ema,
            signals.executed_magnitude,
            signals.executed_magnitude_ema,
        ],
        axis=-1,
    ).astype(np.float32)
