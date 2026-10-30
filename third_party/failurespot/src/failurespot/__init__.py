"""FailureSpot timestamp-level failure detection."""

from .config import ExperimentConfig
from .data import Trajectory
from .models import build_detector
from .signals import ActionSignalNormalizer, compute_action_signals

__all__ = [
    "ActionSignalNormalizer",
    "ExperimentConfig",
    "Trajectory",
    "build_detector",
    "compute_action_signals",
]

__version__ = "0.1.0"
