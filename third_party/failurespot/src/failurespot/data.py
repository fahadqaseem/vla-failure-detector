from __future__ import annotations

import json
from dataclasses import dataclass, replace
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

import numpy as np

from .config import ExperimentConfig


@dataclass(frozen=True)
class Trajectory:
    policy: str
    task_id: int
    episode_id: int
    features: np.ndarray
    action_chunks: np.ndarray
    timestamp_labels: np.ndarray
    trajectory_label: int

    @property
    def key(self) -> str:
        return f"{self.policy}:task{self.task_id}:episode{self.episode_id}"

    def with_features(self, features: np.ndarray) -> "Trajectory":
        return replace(self, features=np.asarray(features, dtype=np.float32))


@dataclass(frozen=True)
class DataSplit:
    train: list[Trajectory]
    seen_evaluation: list[Trajectory]
    unseen_evaluation: list[Trajectory]
    seen_task_ids: list[int]
    unseen_task_ids: list[int]


def round_half_up(value: float) -> int:
    return int(Decimal(str(value)).quantize(Decimal("1"), rounding=ROUND_HALF_UP))


def _scalar(payload: np.lib.npyio.NpzFile, name: str, default=None):
    if name not in payload:
        return default
    value = payload[name]
    return value.item() if np.asarray(value).ndim == 0 else value


def _timestamp_labels(payload: np.lib.npyio.NpzFile, length: int, trajectory_label: int) -> np.ndarray:
    if "timestamp_labels" in payload:
        labels = np.asarray(payload["timestamp_labels"], dtype=np.float32)
        if labels.shape != (length,):
            raise ValueError(f"timestamp_labels must have shape ({length},), got {labels.shape}")
        return labels
    deviation = _scalar(payload, "deviation_index")
    recovery = _scalar(payload, "recovery_index")
    labels = np.zeros(length, dtype=np.float32)
    if deviation is not None and int(deviation) >= 0:
        end = length if recovery is None or int(recovery) < 0 else min(int(recovery), length)
        labels[max(0, int(deviation)):end] = 1.0
    elif trajectory_label == 1:
        raise ValueError("Failed trajectories require timestamp_labels or deviation_index")
    return labels


def load_trajectory(path: str | Path, metadata: dict | None = None) -> Trajectory:
    path = Path(path)
    metadata = metadata or {}
    with np.load(path, allow_pickle=False) as payload:
        features = np.asarray(payload["features"], dtype=np.float32)
        chunks = np.asarray(payload["action_chunks"], dtype=np.float32)
        if chunks.ndim == 2:
            chunks = chunks[:, None, :]
        if features.ndim != 2 or chunks.ndim != 3:
            raise ValueError("features must be [T,F] and action_chunks must be [T,H,D]")
        if len(features) != len(chunks):
            raise ValueError("features and action_chunks must have the same timestamp count")
        trajectory_label = int(
            metadata.get("trajectory_label", _scalar(payload, "trajectory_label", -1))
        )
        if trajectory_label not in {0, 1}:
            success = metadata.get("success", _scalar(payload, "success"))
            if success is None:
                raise ValueError("Each trajectory needs trajectory_label or success")
            trajectory_label = 1 - int(success)
        labels = _timestamp_labels(payload, len(features), trajectory_label)
        policy = str(metadata.get("policy", _scalar(payload, "policy", "unknown")))
        task_id = int(metadata.get("task_id", _scalar(payload, "task_id", -1)))
        episode_id = int(metadata.get("episode_id", _scalar(payload, "episode_id", -1)))
    if task_id < 0 or episode_id < 0:
        raise ValueError(f"Missing task_id or episode_id in {path}")
    return Trajectory(
        policy=policy,
        task_id=task_id,
        episode_id=episode_id,
        features=features,
        action_chunks=chunks,
        timestamp_labels=labels,
        trajectory_label=trajectory_label,
    )


def read_manifest(path: str | Path, expected_policy: str | None = None) -> list[Trajectory]:
    manifest = Path(path).resolve()
    trajectories: list[Trajectory] = []
    with manifest.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            record = json.loads(line)
            data_path = Path(record.pop("path"))
            if not data_path.is_absolute():
                data_path = manifest.parent / data_path
            trajectory = load_trajectory(data_path, record)
            if expected_policy is None or trajectory.policy == expected_policy:
                trajectories.append(trajectory)
    if not trajectories:
        raise ValueError(f"No trajectories found in {manifest}")
    keys = [trajectory.key for trajectory in trajectories]
    if len(keys) != len(set(keys)):
        raise ValueError("Trajectory keys must be unique")
    return trajectories


def validate_trajectories(
    trajectories: list[Trajectory], config: ExperimentConfig
) -> None:
    """Validate the complete LIBERO-10 rollout corpus."""

    expected_tasks = set(range(config.data.task_count))
    task_ids = {trajectory.task_id for trajectory in trajectories}
    if task_ids != expected_tasks:
        raise ValueError(
            f"Expected task IDs {sorted(expected_tasks)}, got {sorted(task_ids)}"
        )
    for task_id in sorted(task_ids):
        count = sum(trajectory.task_id == task_id for trajectory in trajectories)
        if count != config.data.trajectories_per_task:
            raise ValueError(
                f"Task {task_id} must contain {config.data.trajectories_per_task} "
                f"trajectories, got {count}"
            )
    for trajectory in trajectories:
        timestamps = len(trajectory.features)
        if timestamps < 1:
            raise ValueError(f"{trajectory.key} contains no timestamps")
        if trajectory.action_chunks.shape != (
            timestamps,
            config.policy.action_horizon,
            config.policy.action_dimension,
        ):
            raise ValueError(
                f"{trajectory.key} action_chunks has shape "
                f"{trajectory.action_chunks.shape}; expected "
                f"({timestamps}, {config.policy.action_horizon}, "
                f"{config.policy.action_dimension})"
            )
        if (
            config.policy.feature_dimension is not None
            and trajectory.features.shape[1] != config.policy.feature_dimension
        ):
            raise ValueError(
                f"{trajectory.key} feature dimension is "
                f"{trajectory.features.shape[1]}; expected "
                f"{config.policy.feature_dimension}"
            )
        if not np.isin(trajectory.timestamp_labels, (0.0, 1.0)).all():
            raise ValueError(f"{trajectory.key} timestamp labels must be binary")


def split_trajectories(
    trajectories: list[Trajectory],
    seen_task_ids: list[int],
    train_fraction: float,
    seed: int,
) -> DataSplit:
    seen = set(seen_task_ids)
    all_tasks = sorted({trajectory.task_id for trajectory in trajectories})
    unseen_task_ids = [task for task in all_tasks if task not in seen]
    rng = np.random.default_rng(seed)
    train: list[Trajectory] = []
    seen_eval: list[Trajectory] = []
    for task in seen_task_ids:
        task_items = sorted(
            (trajectory for trajectory in trajectories if trajectory.task_id == task),
            key=lambda trajectory: trajectory.episode_id,
        )
        order = rng.permutation(len(task_items))
        count = round_half_up(train_fraction * len(task_items))
        train.extend(task_items[index] for index in order[:count])
        seen_eval.extend(task_items[index] for index in order[count:])
    unseen_eval = [trajectory for trajectory in trajectories if trajectory.task_id not in seen]
    return DataSplit(train, seen_eval, unseen_eval, list(seen_task_ids), unseen_task_ids)


def annotation_budget(fraction: float, seen_task_count: int, trajectories_per_task: int) -> int:
    """Return the nearest realizable global annotation budget."""

    exact = Decimal(str(fraction)) * seen_task_count * trajectories_per_task
    return int(exact.quantize(Decimal("1"), rounding=ROUND_HALF_UP))
