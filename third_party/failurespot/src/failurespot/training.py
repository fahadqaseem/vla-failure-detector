from __future__ import annotations

import json
import random
from pathlib import Path
from typing import Mapping

import numpy as np
import torch
from torch import Tensor, nn
from torch.nn import functional as F
from torch.optim import Adam
from torch.utils.data import DataLoader, Dataset

from .config import ExperimentConfig
from .data import Trajectory


def seed_everything(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def resolve_device(name: str) -> torch.device:
    device = torch.device(name)
    if device.type == "cuda" and not torch.cuda.is_available():
        raise RuntimeError("CUDA is unavailable; use training.device=cpu")
    return device


class LabeledTrajectoryDataset(Dataset):
    def __init__(
        self,
        trajectories: list[Trajectory],
        labels: Mapping[str, np.ndarray],
    ) -> None:
        self.trajectories = trajectories
        self.labels = labels

    def __len__(self) -> int:
        return len(self.trajectories)

    def __getitem__(self, index: int):
        trajectory = self.trajectories[index]
        labels = np.asarray(self.labels[trajectory.key], dtype=np.float32)
        if labels.shape != (len(trajectory.features),):
            raise ValueError(f"Label length mismatch for {trajectory.key}")
        return (
            torch.from_numpy(np.asarray(trajectory.features, dtype=np.float32)),
            torch.from_numpy(labels),
            trajectory.key,
        )


def collate_trajectories(items):
    lengths = [len(features) for features, _, _ in items]
    feature_dimension = items[0][0].shape[-1]
    features = torch.zeros(len(items), max(lengths), feature_dimension)
    labels = torch.zeros(len(items), max(lengths))
    mask = torch.zeros(len(items), max(lengths), dtype=torch.bool)
    keys = []
    for index, (sequence, targets, key) in enumerate(items):
        length = len(sequence)
        features[index, :length] = sequence
        labels[index, :length] = targets
        mask[index, :length] = True
        keys.append(key)
    return {"features": features, "labels": labels, "mask": mask, "keys": keys}


def learning_rate(config: ExperimentConfig, architecture: str) -> float:
    return (
        config.training.mlp_learning_rate
        if architecture == "mlp"
        else config.training.lstm_learning_rate
    )


def train_detector(
    model: nn.Module,
    trajectories: list[Trajectory],
    labels: Mapping[str, np.ndarray],
    config: ExperimentConfig,
    architecture: str,
    epochs: int,
) -> list[float]:
    if not trajectories:
        raise ValueError("Cannot train without trajectories")
    device = resolve_device(config.training.device)
    model.to(device)
    loader = DataLoader(
        LabeledTrajectoryDataset(trajectories, labels),
        batch_size=config.training.batch_size,
        shuffle=True,
        collate_fn=collate_trajectories,
        generator=torch.Generator().manual_seed(config.training.seed),
    )
    optimizer = Adam(
        model.parameters(),
        lr=learning_rate(config, architecture),
        weight_decay=config.training.weight_decay,
    )
    history: list[float] = []
    for _ in range(epochs):
        model.train()
        total_loss, total_timestamps = 0.0, 0
        for batch in loader:
            features = batch["features"].to(device)
            targets = batch["labels"].to(device)
            mask = batch["mask"].to(device)
            optimizer.zero_grad(set_to_none=True)
            logits = model(features, mask)
            loss = F.binary_cross_entropy_with_logits(logits[mask], targets[mask])
            loss.backward()
            if config.training.gradient_clip_norm is not None:
                torch.nn.utils.clip_grad_norm_(
                    model.parameters(), config.training.gradient_clip_norm
                )
            optimizer.step()
            count = int(mask.sum())
            total_loss += float(loss.detach()) * count
            total_timestamps += count
        history.append(total_loss / max(total_timestamps, 1))
    return history


@torch.no_grad()
def predict_scores(
    model: nn.Module,
    trajectories: list[Trajectory],
    device_name: str,
) -> dict[str, np.ndarray]:
    device = resolve_device(device_name)
    model.to(device).eval()
    scores: dict[str, np.ndarray] = {}
    for trajectory in trajectories:
        features = torch.from_numpy(trajectory.features).float().unsqueeze(0).to(device)
        logits = model(features)
        scores[trajectory.key] = torch.sigmoid(logits[0]).cpu().numpy().astype(np.float32)
    return scores


def timestamp_labels(trajectories: list[Trajectory]) -> dict[str, np.ndarray]:
    return {
        trajectory.key: np.asarray(trajectory.timestamp_labels, dtype=np.float32)
        for trajectory in trajectories
    }


def repeated_trajectory_labels(
    trajectories: list[Trajectory],
) -> dict[str, np.ndarray]:
    return {
        trajectory.key: np.full(
            len(trajectory.features), trajectory.trajectory_label, dtype=np.float32
        )
        for trajectory in trajectories
    }


def save_checkpoint(
    path: str | Path,
    model: nn.Module,
    config: ExperimentConfig,
    architecture: str,
    method: str,
    history: list[float],
    selected_keys: list[str] | None = None,
) -> Path:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    torch.save(
        {
            "format_version": 1,
            "architecture": architecture,
            "method": method,
            "config": config.to_dict(),
            "history": history,
            "selected_trajectory_keys": selected_keys or [],
            "model_state_dict": model.state_dict(),
        },
        destination,
    )
    metadata = {
        "architecture": architecture,
        "method": method,
        "selected_trajectory_keys": selected_keys or [],
        "history": history,
        "config": config.to_dict(),
    }
    destination.with_suffix(".json").write_text(
        json.dumps(metadata, indent=2), encoding="utf-8"
    )
    return destination
