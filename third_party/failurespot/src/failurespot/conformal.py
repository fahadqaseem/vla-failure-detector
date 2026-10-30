from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .data import Trajectory
from .metrics import balanced_accuracy


def resample_normalized_time(values: np.ndarray, points: int) -> np.ndarray:
    values = np.asarray(values, dtype=np.float64)
    if len(values) == 1:
        return np.full(points, values[0], dtype=np.float64)
    source = np.linspace(0.0, 1.0, len(values))
    target = np.linspace(0.0, 1.0, points)
    return np.interp(target, source, values)


@dataclass
class FunctionalConformalBand:
    regression_curves: np.ndarray
    calibration_curves: np.ndarray

    @classmethod
    def fit(
        cls,
        trajectories: list[Trajectory],
        scores: dict[str, np.ndarray],
        normalized_time_points: int = 100,
        regression_fraction: float = 0.30,
        seed: int = 0,
    ) -> "FunctionalConformalBand":
        successful = [
            trajectory for trajectory in trajectories if trajectory.trajectory_label == 0
        ]
        if not successful:
            raise ValueError("Conformal calibration requires successful held-out trajectories")
        curves = np.stack(
            [
                resample_normalized_time(scores[trajectory.key], normalized_time_points)
                for trajectory in successful
            ]
        )
        if len(curves) == 1:
            return cls(curves, curves)
        rng = np.random.default_rng(seed)
        curves = curves[rng.permutation(len(curves))]
        regression_count = max(1, int(np.floor(len(curves) * regression_fraction)))
        regression_count = min(regression_count, len(curves) - 1)
        return cls(curves[:regression_count], curves[regression_count:])

    @staticmethod
    def _finite_sample_quantile(values: np.ndarray, alpha: float) -> float:
        ordered = np.sort(np.asarray(values, dtype=np.float64).reshape(-1))
        rank = int(np.ceil((len(ordered) + 1) * (1.0 - alpha)))
        return float(ordered[min(max(rank, 1), len(ordered)) - 1])

    def _modulation(self, center: np.ndarray, alpha: float) -> np.ndarray:
        deviations = np.abs(self.regression_curves - center)
        suprema = deviations.max(axis=1)
        rank = int(np.ceil((len(suprema) + 1) * (1.0 - alpha)))
        if rank > len(suprema):
            retained = deviations
        else:
            radius = np.sort(suprema)[rank - 1]
            retained = deviations[suprema <= radius]
        return retained.max(axis=0) + 1e-8

    def normalized_threshold(self, alpha: float) -> np.ndarray:
        if not 0.0 < alpha < 1.0:
            raise ValueError("alpha must be in (0,1)")
        center = self.regression_curves.mean(axis=0)
        modulation = self._modulation(center, alpha)
        nonconformity = (
            (self.calibration_curves - center) / modulation
        ).max(axis=1)
        width = self._finite_sample_quantile(nonconformity, alpha)
        return center + width * modulation

    def threshold(self, alpha: float, length: int) -> np.ndarray:
        normalized = self.normalized_threshold(alpha)
        return resample_normalized_time(normalized, length)


def conformal_sweep(
    band: FunctionalConformalBand,
    trajectories: list[Trajectory],
    scores: dict[str, np.ndarray],
    alphas: np.ndarray,
) -> list[dict[str, float]]:
    labels = np.concatenate([trajectory.timestamp_labels for trajectory in trajectories])
    output: list[dict[str, float]] = []
    failed = [trajectory for trajectory in trajectories if trajectory.trajectory_label == 1]
    for alpha in alphas:
        predictions = []
        detected_onsets = []
        for trajectory in trajectories:
            trajectory_scores = scores[trajectory.key]
            threshold = band.threshold(float(alpha), len(trajectory_scores))
            alarms = trajectory_scores >= threshold
            predictions.append(alarms.astype(np.int64))
            if trajectory.trajectory_label == 1:
                indices = np.flatnonzero(alarms)
                detected_onsets.append(
                    float(indices[0] / max(len(alarms) - 1, 1)) if len(indices) else 1.0
                )
        output.append(
            {
                "alpha": float(alpha),
                "timestamp_balanced_accuracy": balanced_accuracy(
                    labels, np.concatenate(predictions)
                ),
                "mean_normalized_detection_time": (
                    float(np.mean(detected_onsets)) if failed else float("nan")
                ),
            }
        )
    return output
