from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

import yaml


@dataclass
class PolicyConfig:
    name: str = "pi0"
    action_horizon: int = 50
    execution_horizon: int = 5
    action_dimension: int = 7
    feature_dimension: int | None = None


@dataclass
class DataConfig:
    manifest: str = "manifests/trajectories.jsonl"
    task_count: int = 10
    trajectories_per_task: int = 50
    seen_task_count: int = 3
    seen_train_fraction: float = 0.60
    annotation_fraction: float = 0.15
    seen_task_splits: list[list[int]] = field(
        default_factory=lambda: [[4, 6, 2], [8, 4, 7], [2, 0, 7]]
    )


@dataclass
class SignalConfig:
    ema_beta: float = 0.8
    consistency_weight: float = 1.0
    full_magnitude_weight: float = 1.0
    executed_magnitude_weight: float = 1.0
    lower_percentile: float = 1.0
    upper_percentile: float = 99.0


@dataclass
class ModelConfig:
    architecture: str = "mlp"
    hidden_dimension: int = 256
    layer_count: int = 2
    dropout: float = 0.0


@dataclass
class TrainingConfig:
    weak_pretrain_epochs: int = 1000
    fine_tune_epochs: int = 1000
    baseline_epochs: int = 200
    batch_size: int = 16
    mlp_learning_rate: float = 3e-5
    lstm_learning_rate: float = 1e-4
    weight_decay: float = 0.0
    gradient_clip_norm: float | None = 1.0
    seed: int = 0
    device: str = "cuda"


@dataclass
class LogpZOConfig:
    epochs: int = 50
    batch_size: int = 32
    learning_rate: float = 1e-4
    inner_dimension: int = 20
    time_embedding_dimension: int = 128
    channel_dimensions: list[int] = field(default_factory=lambda: [256, 512, 1024])
    group_count: int = 8
    forward_chunk_size: int = 512


@dataclass
class ConformalConfig:
    alpha_values: list[float] = field(
        default_factory=lambda: [
            0.02,
            0.05,
            0.10,
            0.15,
            0.20,
            0.25,
            0.30,
            0.35,
            0.40,
            0.45,
            0.50,
            0.60,
            0.70,
            0.80,
            0.90,
        ]
    )
    normalized_time_points: int = 100
    regression_fraction: float = 0.30


@dataclass
class OutputConfig:
    directory: str = "outputs/failurespot"


@dataclass
class ExperimentConfig:
    policy: PolicyConfig = field(default_factory=PolicyConfig)
    data: DataConfig = field(default_factory=DataConfig)
    signals: SignalConfig = field(default_factory=SignalConfig)
    model: ModelConfig = field(default_factory=ModelConfig)
    training: TrainingConfig = field(default_factory=TrainingConfig)
    logpzo: LogpZOConfig = field(default_factory=LogpZOConfig)
    conformal: ConformalConfig = field(default_factory=ConformalConfig)
    output: OutputConfig = field(default_factory=OutputConfig)

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> "ExperimentConfig":
        return cls(
            policy=PolicyConfig(**raw.get("policy", {})),
            data=DataConfig(**raw.get("data", {})),
            signals=SignalConfig(**raw.get("signals", {})),
            model=ModelConfig(**raw.get("model", {})),
            training=TrainingConfig(**raw.get("training", {})),
            logpzo=LogpZOConfig(**raw.get("logpzo", {})),
            conformal=ConformalConfig(**raw.get("conformal", {})),
            output=OutputConfig(**raw.get("output", {})),
        )

    @classmethod
    def load(cls, path: str | Path) -> "ExperimentConfig":
        path = Path(path)
        with path.open("r", encoding="utf-8") as handle:
            raw = json.load(handle) if path.suffix.lower() == ".json" else yaml.safe_load(handle)
        if not isinstance(raw, dict):
            raise ValueError(f"Expected a mapping in {path}")
        config = cls.from_dict(raw)
        config.validate()
        return config

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    def validate(self) -> None:
        if self.policy.action_horizon < 1:
            raise ValueError("action_horizon must be positive")
        if not 1 <= self.policy.execution_horizon <= self.policy.action_horizon:
            raise ValueError("execution_horizon must be in [1, action_horizon]")
        if self.policy.action_dimension != 7:
            raise ValueError("The action space must be seven-dimensional")
        expected_horizons = {
            "pi0": (50, 5),
            "pi0_fast": (10, 5),
            "openvla": (1, 1),
        }
        if self.policy.name in expected_horizons:
            expected = expected_horizons[self.policy.name]
            actual = (self.policy.action_horizon, self.policy.execution_horizon)
            if actual != expected:
                raise ValueError(
                    f"Expected H,K={expected} for {self.policy.name}, got {actual}"
                )
        if self.data.task_count != 10 or self.data.seen_task_count != 3:
            raise ValueError("The protocol uses 3 seen and 7 unseen LIBERO-10 tasks")
        if self.data.trajectories_per_task != 50:
            raise ValueError("Each task must contain exactly 50 trajectories")
        if self.data.seen_train_fraction != 0.60:
            raise ValueError("Each seen task uses 60% of trajectories for training")
        if self.data.annotation_fraction != 0.15:
            raise ValueError("The annotation budget is 15% of seen-task trajectories")
        if not 0.0 <= self.signals.ema_beta < 1.0:
            raise ValueError("ema_beta must be in [0, 1)")
        if self.signals.ema_beta != 0.8:
            raise ValueError("EMA beta must be 0.8")
        if self.signals.consistency_weight != 1.0:
            raise ValueError("Equation 3 fixes the consistency coefficient to one")
        if (
            self.signals.lower_percentile != 1.0
            or self.signals.upper_percentile != 99.0
        ):
            raise ValueError("Normalization uses training-only 1st/99th percentiles")
        if self.model.architecture not in {"mlp", "lstm"}:
            raise ValueError("architecture must be 'mlp' or 'lstm'")
        if self.logpzo.epochs < 1 or self.logpzo.batch_size < 1:
            raise ValueError("LogpZO epochs and batch_size must be positive")
        if self.logpzo.inner_dimension < 1:
            raise ValueError("LogpZO inner_dimension must be positive")
        if not self.logpzo.channel_dimensions:
            raise ValueError("LogpZO channel_dimensions cannot be empty")
        expected_alphas = [
            0.02, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35,
            0.40, 0.45, 0.50, 0.60, 0.70, 0.80, 0.90,
        ]
        if self.conformal.alpha_values != expected_alphas:
            raise ValueError(f"The conformal sweep uses {expected_alphas}")
        if not 0.0 < self.conformal.regression_fraction < 1.0:
            raise ValueError("regression_fraction must be in (0,1)")
