from __future__ import annotations

import torch
from torch import Tensor, nn

from .config import ModelConfig


class MLPDetector(nn.Module):
    """Timestamp-wise multilayer perceptron returning failure logits."""

    def __init__(
        self,
        input_dimension: int,
        hidden_dimension: int = 256,
        layer_count: int = 2,
        dropout: float = 0.0,
    ) -> None:
        super().__init__()
        if layer_count < 1:
            raise ValueError("layer_count must be positive")
        layers: list[nn.Module] = []
        dimension = input_dimension
        for _ in range(layer_count):
            layers.extend(
                [
                    nn.Linear(dimension, hidden_dimension),
                    nn.ReLU(),
                    nn.Dropout(dropout),
                ]
            )
            dimension = hidden_dimension
        layers.append(nn.Linear(dimension, 1))
        self.network = nn.Sequential(*layers)

    def forward(self, features: Tensor, mask: Tensor | None = None) -> Tensor:
        del mask
        return self.network(features).squeeze(-1)


class LSTMDetector(nn.Module):
    """Causal timestamp detector over all representations observed so far."""

    def __init__(
        self,
        input_dimension: int,
        hidden_dimension: int = 256,
        layer_count: int = 1,
        dropout: float = 0.0,
    ) -> None:
        super().__init__()
        recurrent_dropout = dropout if layer_count > 1 else 0.0
        self.recurrent = nn.LSTM(
            input_dimension,
            hidden_dimension,
            num_layers=layer_count,
            batch_first=True,
            dropout=recurrent_dropout,
        )
        self.dropout = nn.Dropout(dropout)
        self.output = nn.Linear(hidden_dimension, 1)

    def forward(self, features: Tensor, mask: Tensor | None = None) -> Tensor:
        del mask
        states, _ = self.recurrent(features)
        return self.output(self.dropout(states)).squeeze(-1)


def build_detector(
    input_dimension: int,
    config: ModelConfig,
    architecture: str | None = None,
) -> nn.Module:
    name = architecture or config.architecture
    if name == "mlp":
        return MLPDetector(
            input_dimension,
            config.hidden_dimension,
            config.layer_count,
            config.dropout,
        )
    if name == "lstm":
        return LSTMDetector(
            input_dimension,
            config.hidden_dimension,
            config.layer_count,
            config.dropout,
        )
    raise ValueError(f"Unknown detector architecture: {name}")
