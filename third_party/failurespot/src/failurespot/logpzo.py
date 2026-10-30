from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np
import torch
from torch import Tensor, nn
from torch.nn import functional as F
from torch.optim import Adam
from torch.utils.data import DataLoader, TensorDataset

from .config import ExperimentConfig, LogpZOConfig
from .data import Trajectory
from .training import resolve_device, seed_everything


class SinusoidalTimeEmbedding(nn.Module):
    def __init__(self, dimension: int) -> None:
        super().__init__()
        if dimension < 4 or dimension % 2:
            raise ValueError("time embedding dimension must be even and at least four")
        self.dimension = dimension

    def forward(self, timesteps: Tensor) -> Tensor:
        half = self.dimension // 2
        scale = math.log(10_000.0) / (half - 1)
        frequencies = torch.exp(
            torch.arange(half, device=timesteps.device) * -scale
        )
        phases = timesteps.float()[:, None] * frequencies[None, :]
        return torch.cat((phases.sin(), phases.cos()), dim=-1)


def compatible_group_count(channels: int, requested: int) -> int:
    for groups in range(min(channels, requested), 0, -1):
        if channels % groups == 0:
            return groups
    return 1


class ConvolutionBlock(nn.Module):
    def __init__(self, input_channels: int, output_channels: int, groups: int) -> None:
        super().__init__()
        self.network = nn.Sequential(
            nn.Conv1d(input_channels, output_channels, 3, padding=1),
            nn.GroupNorm(compatible_group_count(output_channels, groups), output_channels),
            nn.Mish(),
        )

    def forward(self, values: Tensor) -> Tensor:
        return self.network(values)


class TimeConditionedResidualBlock(nn.Module):
    def __init__(
        self,
        input_channels: int,
        output_channels: int,
        time_dimension: int,
        groups: int,
    ) -> None:
        super().__init__()
        self.first = ConvolutionBlock(input_channels, output_channels, groups)
        self.second = ConvolutionBlock(output_channels, output_channels, groups)
        self.time_projection = nn.Sequential(
            nn.Mish(), nn.Linear(time_dimension, output_channels)
        )
        self.residual = (
            nn.Conv1d(input_channels, output_channels, 1)
            if input_channels != output_channels
            else nn.Identity()
        )

    def forward(self, values: Tensor, time_embedding: Tensor) -> Tensor:
        hidden = self.first(values)
        hidden = hidden + self.time_projection(time_embedding).unsqueeze(-1)
        return self.second(hidden) + self.residual(values)


class FlowMatchingUNet1D(nn.Module):
    """Time-conditioned 1D U-Net used by the LogpZO comparison method."""

    def __init__(self, config: LogpZOConfig) -> None:
        super().__init__()
        channels = [config.inner_dimension, *config.channel_dimensions]
        time_dimension = config.time_embedding_dimension
        self.time_encoder = nn.Sequential(
            SinusoidalTimeEmbedding(time_dimension),
            nn.Linear(time_dimension, time_dimension * 4),
            nn.Mish(),
            nn.Linear(time_dimension * 4, time_dimension),
        )
        self.down_blocks = nn.ModuleList()
        for index, (input_channels, output_channels) in enumerate(
            zip(channels[:-1], channels[1:])
        ):
            last = index == len(channels) - 2
            self.down_blocks.append(
                nn.ModuleList(
                    [
                        TimeConditionedResidualBlock(
                            input_channels,
                            output_channels,
                            time_dimension,
                            config.group_count,
                        ),
                        TimeConditionedResidualBlock(
                            output_channels,
                            output_channels,
                            time_dimension,
                            config.group_count,
                        ),
                        nn.Identity()
                        if last
                        else nn.Conv1d(output_channels, output_channels, 3, 2, 1),
                    ]
                )
            )
        middle_channels = channels[-1]
        self.middle = nn.ModuleList(
            [
                TimeConditionedResidualBlock(
                    middle_channels,
                    middle_channels,
                    time_dimension,
                    config.group_count,
                ),
                TimeConditionedResidualBlock(
                    middle_channels,
                    middle_channels,
                    time_dimension,
                    config.group_count,
                ),
            ]
        )
        self.up_blocks = nn.ModuleList()
        down_pairs = list(zip(channels[:-1], channels[1:]))
        for input_channels, output_channels in reversed(down_pairs[1:]):
            self.up_blocks.append(
                nn.ModuleList(
                    [
                        TimeConditionedResidualBlock(
                            output_channels * 2,
                            input_channels,
                            time_dimension,
                            config.group_count,
                        ),
                        TimeConditionedResidualBlock(
                            input_channels,
                            input_channels,
                            time_dimension,
                            config.group_count,
                        ),
                        nn.ConvTranspose1d(input_channels, input_channels, 4, 2, 1),
                    ]
                )
            )
        first_channels = config.channel_dimensions[0]
        self.output = nn.Sequential(
            ConvolutionBlock(first_channels, first_channels, config.group_count),
            nn.Conv1d(first_channels, config.inner_dimension, 1),
        )

    def forward(self, sequences: Tensor, timesteps: Tensor) -> Tensor:
        hidden = sequences.transpose(1, 2)
        time_embedding = self.time_encoder(timesteps)
        skips: list[Tensor] = []
        for first, second, downsample in self.down_blocks:
            hidden = first(hidden, time_embedding)
            hidden = second(hidden, time_embedding)
            skips.append(hidden)
            hidden = downsample(hidden)
        for block in self.middle:
            hidden = block(hidden, time_embedding)
        for first, second, upsample in self.up_blocks:
            hidden = torch.cat((hidden, skips.pop()), dim=1)
            hidden = first(hidden, time_embedding)
            hidden = second(hidden, time_embedding)
            hidden = upsample(hidden)
        return self.output(hidden).transpose(1, 2)


def reshape_features(features: Tensor, inner_dimension: int) -> Tensor:
    values = features.reshape(len(features), -1)
    feature_padding = (-values.shape[1]) % inner_dimension
    if feature_padding:
        values = F.pad(values, (0, feature_padding))
    sequence_length = values.shape[1] // inner_dimension
    sequence_padding = (-sequence_length) % 4
    if sequence_padding:
        values = F.pad(values, (0, sequence_padding * inner_dimension))
    return values.reshape(len(values), -1, inner_dimension)


class LogpZODetector(nn.Module):
    """Success/failure flow-density ratio detector from FAIL-Detect."""

    def __init__(self, config: LogpZOConfig) -> None:
        super().__init__()
        self.config = config
        self.success_flow = FlowMatchingUNet1D(config)
        self.failure_flow = FlowMatchingUNet1D(config)

    def flow_matching_loss(self, network: nn.Module, features: Tensor) -> Tensor:
        clean = reshape_features(features, self.config.inner_dimension)
        noise = torch.randn_like(clean)
        target_velocity = noise - clean
        time = torch.rand(len(clean), device=clean.device)
        interpolated = clean + time[:, None, None] * target_velocity
        prediction = network(interpolated, (time * 100.0).long())
        return F.mse_loss(prediction, target_velocity)

    def _distribution_error(self, network: nn.Module, features: Tensor) -> Tensor:
        values = reshape_features(features, self.config.inner_dimension)
        timesteps = torch.zeros(len(values), dtype=torch.long, device=values.device)
        velocity = network(values, timesteps)
        return (values + velocity).square().flatten(1).sum(dim=1)

    def forward(self, features: Tensor) -> Tensor:
        success_error = self._distribution_error(self.success_flow, features)
        failure_error = self._distribution_error(self.failure_flow, features)
        return success_error - failure_error


@dataclass
class LogpZOTrainingResult:
    model: LogpZODetector
    history: list[float]


def fit_logpzo(
    trajectories: list[Trajectory], config: ExperimentConfig
) -> LogpZOTrainingResult:
    seed_everything(config.training.seed)
    device = resolve_device(config.training.device)
    features = torch.from_numpy(
        np.concatenate([trajectory.features for trajectory in trajectories])
    ).float()
    labels = torch.from_numpy(
        np.concatenate(
            [
                np.full(len(trajectory.features), trajectory.trajectory_label)
                for trajectory in trajectories
            ]
        )
    ).long()
    if not (labels == 0).any() or not (labels == 1).any():
        raise ValueError("LogpZO requires successful and failed training trajectories")
    loader = DataLoader(
        TensorDataset(features, labels),
        batch_size=config.logpzo.batch_size,
        shuffle=True,
        generator=torch.Generator().manual_seed(config.training.seed),
    )
    model = LogpZODetector(config.logpzo).to(device)
    optimizer = Adam(model.parameters(), lr=config.logpzo.learning_rate)
    history: list[float] = []
    for _ in range(config.logpzo.epochs):
        model.train()
        total_loss, batches = 0.0, 0
        for batch_features, batch_labels in loader:
            batch_features = batch_features.to(device)
            batch_labels = batch_labels.to(device)
            losses = []
            if (batch_labels == 0).any():
                losses.append(
                    model.flow_matching_loss(
                        model.success_flow, batch_features[batch_labels == 0]
                    )
                )
            if (batch_labels == 1).any():
                losses.append(
                    model.flow_matching_loss(
                        model.failure_flow, batch_features[batch_labels == 1]
                    )
                )
            loss = torch.stack(losses).sum()
            optimizer.zero_grad(set_to_none=True)
            loss.backward()
            optimizer.step()
            total_loss += float(loss.detach())
            batches += 1
        history.append(total_loss / max(batches, 1))
    return LogpZOTrainingResult(model, history)


@torch.no_grad()
def score_logpzo(
    model: LogpZODetector,
    trajectories: list[Trajectory],
    device_name: str,
) -> dict[str, np.ndarray]:
    device = resolve_device(device_name)
    model.to(device).eval()
    output: dict[str, np.ndarray] = {}
    chunk_size = model.config.forward_chunk_size
    for trajectory in trajectories:
        features = torch.from_numpy(trajectory.features).float().to(device)
        parts = []
        step = chunk_size if chunk_size > 0 else len(features)
        for start in range(0, len(features), step):
            parts.append(model(features[start : start + step]).cpu())
        output[trajectory.key] = torch.cat(parts).numpy().astype(np.float32)
    return output
