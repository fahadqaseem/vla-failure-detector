from __future__ import annotations

from pathlib import Path

import numpy as np

from .config import ExperimentConfig
from .data import Trajectory, split_trajectories
from .experiment import (
    run_action_probe,
    run_logpzo,
    run_score_baseline,
    run_trainable,
)


def synthetic_trajectories(seed: int = 0) -> list[Trajectory]:
    rng = np.random.default_rng(seed)
    trajectories: list[Trajectory] = []
    for task_id in range(10):
        for episode_id in range(50):
            length = 4 + episode_id % 2
            failed = int(episode_id % 2 == 1)
            labels = np.zeros(length, dtype=np.float32)
            if failed:
                labels[length // 2:] = 1.0
            features = rng.normal(size=(length, 4)).astype(np.float32)
            features += labels[:, None] * 0.5
            chunks = rng.normal(scale=0.1, size=(length, 2, 7)).astype(np.float32)
            if failed:
                chunks[length // 2:] += 0.5
            trajectories.append(
                Trajectory(
                    policy="smoke",
                    task_id=task_id,
                    episode_id=episode_id,
                    features=features,
                    action_chunks=chunks,
                    timestamp_labels=labels,
                    trajectory_label=failed,
                )
            )
    return trajectories


def smoke_config(output: str | Path) -> ExperimentConfig:
    config = ExperimentConfig.from_dict(
        {
            "policy": {
                "name": "smoke",
                "action_horizon": 2,
                "execution_horizon": 1,
                "action_dimension": 7,
                "feature_dimension": 4,
            },
            "model": {
                "hidden_dimension": 8,
                "layer_count": 1,
                "dropout": 0.0,
            },
            "training": {
                "weak_pretrain_epochs": 1,
                "fine_tune_epochs": 1,
                "baseline_epochs": 1,
                "batch_size": 32,
                "mlp_learning_rate": 0.01,
                "lstm_learning_rate": 0.01,
                "seed": 0,
                "device": "cpu",
            },
            "conformal": {"normalized_time_points": 8},
            "logpzo": {
                "epochs": 1,
                "batch_size": 256,
                "learning_rate": 0.001,
                "inner_dimension": 2,
                "time_embedding_dimension": 8,
                "channel_dimensions": [8, 16],
                "group_count": 4,
                "forward_chunk_size": 256,
            },
            "output": {"directory": str(output)},
        }
    )
    config.validate()
    return config


def run_smoke(output: str | Path) -> dict:
    config = smoke_config(output)
    trajectories = synthetic_trajectories()
    split = split_trajectories(trajectories, [0, 1, 2], 0.60, 0)
    results = {}
    for architecture in ("mlp", "lstm"):
        destination = Path(output) / architecture
        results[architecture] = run_trainable(
            "failurespot", architecture, split, config, destination
        )
        assert results[architecture]["selected_count"] == 23
        assert "seen" in results[architecture]["metrics"]
        assert "unseen" in results[architecture]["metrics"]
        for method in (
            "weak_only",
            "weak_random_finetune",
            "trajectory_active_finetune",
            "safe",
            "supervised_random",
        ):
            key = f"{method}_{architecture}"
            results[key] = run_trainable(
                method,
                architecture,
                split,
                config,
                Path(output) / key,
            )
        results[f"actprobe_{architecture}"] = run_action_probe(
            architecture,
            split,
            config,
            Path(output) / f"actprobe_{architecture}",
        )
    results["stac"] = run_score_baseline("stac", split, config)
    results["logpzo"] = run_logpzo(split, config, Path(output) / "logpzo")
    return results
