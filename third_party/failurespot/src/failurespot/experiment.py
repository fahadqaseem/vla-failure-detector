from __future__ import annotations

import copy
import json
from pathlib import Path

import numpy as np
import torch

from .baselines import stac_scores
from .config import ExperimentConfig
from .conformal import FunctionalConformalBand, conformal_sweep
from .data import DataSplit, Trajectory, annotation_budget
from .metrics import evaluate_scores
from .logpzo import fit_logpzo, score_logpzo
from .models import build_detector
from .selection import select_by_uncertainty, select_random
from .signals import ActionSignalNormalizer, action_probe_features
from .training import (
    predict_scores,
    repeated_trajectory_labels,
    save_checkpoint,
    seed_everything,
    timestamp_labels,
    train_detector,
)


TRAINABLE_METHODS = {
    "failurespot",
    "weak_only",
    "weak_random_finetune",
    "trajectory_active_finetune",
    "supervised_random",
    "safe",
}


def _weak_labels(
    trajectories: list[Trajectory],
    config: ExperimentConfig,
) -> tuple[dict[str, np.ndarray], ActionSignalNormalizer]:
    normalizer = ActionSignalNormalizer.fit(
        trajectories, config.policy.execution_horizon, config.signals
    )
    labels = {
        trajectory.key: normalizer.labels_for(
            trajectory, config.policy.execution_horizon, config.signals
        )
        for trajectory in trajectories
    }
    return labels, normalizer


def _budget(config: ExperimentConfig, annotation_fraction: float | None = None) -> int:
    return annotation_budget(
        config.data.annotation_fraction
        if annotation_fraction is None
        else annotation_fraction,
        config.data.seen_task_count,
        config.data.trajectories_per_task,
    )


def fit_trainable_method(
    method: str,
    architecture: str,
    split: DataSplit,
    config: ExperimentConfig,
    output: Path,
    annotation_fraction: float | None = None,
) -> tuple[object, list[Trajectory], list[float]]:
    if method not in TRAINABLE_METHODS:
        raise ValueError(f"Unknown trainable method: {method}")
    seed_everything(config.training.seed)
    feature_dimension = split.train[0].features.shape[-1]
    model = build_detector(feature_dimension, config.model, architecture)
    budget = _budget(config, annotation_fraction)
    if budget > len(split.train):
        raise ValueError(
            f"Annotation budget {budget} exceeds {len(split.train)} training trajectories"
        )
    history: list[float] = []
    selected: list[Trajectory] = []

    if method in {"failurespot", "weak_only", "weak_random_finetune"}:
        labels, _ = _weak_labels(split.train, config)
        history.extend(
            train_detector(
                model,
                split.train,
                labels,
                config,
                architecture,
                config.training.weak_pretrain_epochs,
            )
        )
        if method == "failurespot":
            acquisition_scores = predict_scores(
                model, split.train, config.training.device
            )
            selected = select_by_uncertainty(split.train, acquisition_scores, budget)
        elif method == "weak_random_finetune":
            selected = select_random(split.train, budget, config.training.seed + 1701)
    elif method in {"trajectory_active_finetune", "safe"}:
        pretrain_epochs = (
            config.training.baseline_epochs
            if method == "safe"
            else config.training.weak_pretrain_epochs
        )
        history.extend(
            train_detector(
                model,
                split.train,
                repeated_trajectory_labels(split.train),
                config,
                architecture,
                pretrain_epochs,
            )
        )
        if method == "trajectory_active_finetune":
            acquisition_scores = predict_scores(
                model, split.train, config.training.device
            )
            selected = select_by_uncertainty(split.train, acquisition_scores, budget)
    elif method == "supervised_random":
        selected = select_random(split.train, budget, config.training.seed + 2903)

    if selected:
        history.extend(
            train_detector(
                model,
                selected,
                timestamp_labels(selected),
                config,
                architecture,
                (
                    config.training.baseline_epochs
                    if method == "supervised_random"
                    else config.training.fine_tune_epochs
                ),
            )
        )
    save_checkpoint(
        output / "model.pt",
        model,
        config,
        architecture,
        method,
        history,
        [trajectory.key for trajectory in selected],
    )
    return model, selected, history


def evaluate_score_traces(
    scores: dict[str, np.ndarray],
    split: DataSplit,
    config: ExperimentConfig,
) -> dict:
    result = {
        "seen": evaluate_scores(split.seen_evaluation, scores),
        "unseen": evaluate_scores(split.unseen_evaluation, scores),
    }
    if any(t.trajectory_label == 0 for t in split.seen_evaluation):
        band = FunctionalConformalBand.fit(
            split.seen_evaluation,
            scores,
            config.conformal.normalized_time_points,
            config.conformal.regression_fraction,
            config.training.seed,
        )
        alphas = np.asarray(config.conformal.alpha_values, dtype=np.float64)
        result["conformal_seen"] = conformal_sweep(
            band, split.seen_evaluation, scores, alphas
        )
        result["conformal_unseen"] = conformal_sweep(
            band, split.unseen_evaluation, scores, alphas
        )
    return result


def evaluate_model(
    model,
    split: DataSplit,
    config: ExperimentConfig,
) -> dict:
    all_evaluation = split.seen_evaluation + split.unseen_evaluation
    scores = predict_scores(model, all_evaluation, config.training.device)
    return evaluate_score_traces(scores, split, config)


def run_trainable(
    method: str,
    architecture: str,
    split: DataSplit,
    config: ExperimentConfig,
    output: Path,
    annotation_fraction: float | None = None,
) -> dict:
    model, selected, history = fit_trainable_method(
        method, architecture, split, config, output, annotation_fraction
    )
    return {
        "method": method,
        "architecture": architecture,
        "seed": config.training.seed,
        "selected_count": len(selected),
        "selected_keys": [trajectory.key for trajectory in selected],
        "final_training_loss": history[-1] if history else None,
        "metrics": evaluate_model(model, split, config),
    }


def run_action_probe(
    architecture: str,
    split: DataSplit,
    config: ExperimentConfig,
    output: Path,
) -> dict:
    seed_everything(config.training.seed)
    transform = lambda items: [
        trajectory.with_features(
            action_probe_features(
                trajectory,
                config.policy.execution_horizon,
                config.signals.ema_beta,
            )
        )
        for trajectory in items
    ]
    probe_split = DataSplit(
        transform(split.train),
        transform(split.seen_evaluation),
        transform(split.unseen_evaluation),
        split.seen_task_ids,
        split.unseen_task_ids,
    )
    model = build_detector(6, config.model, architecture)
    history = train_detector(
        model,
        probe_split.train,
        repeated_trajectory_labels(probe_split.train),
        config,
        architecture,
        config.training.baseline_epochs,
    )
    save_checkpoint(
        output / "model.pt", model, config, architecture, "actprobe", history
    )
    return {
        "method": "actprobe",
        "architecture": architecture,
        "seed": config.training.seed,
        "selected_count": 0,
        "metrics": evaluate_model(model, probe_split, config),
    }


def run_score_baseline(
    method: str,
    split: DataSplit,
    config: ExperimentConfig,
) -> dict:
    evaluation = split.seen_evaluation + split.unseen_evaluation
    if method == "stac":
        if config.policy.action_horizon == config.policy.execution_horizon == 1:
            return {"method": "stac", "architecture": "none", "applicable": False}
        scores = stac_scores(
            evaluation,
            config.policy.execution_horizon,
            config.signals.ema_beta,
        )
    else:
        raise ValueError(f"Unknown score baseline: {method}")
    return {
        "method": method,
        "architecture": "none",
        "applicable": True,
        "seed": config.training.seed,
        "selected_count": 0,
        "metrics": evaluate_score_traces(scores, split, config),
    }


def run_logpzo(split: DataSplit, config: ExperimentConfig, output: Path) -> dict:
    training = fit_logpzo(split.train, config)
    destination = Path(output)
    destination.mkdir(parents=True, exist_ok=True)
    torch_payload = {
        "format_version": 1,
        "method": "logpzo",
        "config": config.to_dict(),
        "history": training.history,
        "model_state_dict": training.model.state_dict(),
    }
    torch.save(torch_payload, destination / "model.pt")
    evaluation = split.seen_evaluation + split.unseen_evaluation
    scores = score_logpzo(training.model, evaluation, config.training.device)
    return {
        "method": "logpzo",
        "architecture": "flow_unet",
        "applicable": True,
        "seed": config.training.seed,
        "selected_count": 0,
        "final_training_loss": training.history[-1],
        "metrics": evaluate_score_traces(scores, split, config),
    }


def write_result(path: str | Path, payload: dict) -> Path:
    def safe(value):
        if isinstance(value, float) and not np.isfinite(value):
            return None
        if isinstance(value, dict):
            return {key: safe(item) for key, item in value.items()}
        if isinstance(value, list):
            return [safe(item) for item in value]
        return value

    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(safe(payload), indent=2), encoding="utf-8")
    return destination


def clone_config(config: ExperimentConfig) -> ExperimentConfig:
    return ExperimentConfig.from_dict(copy.deepcopy(config.to_dict()))
