import numpy as np

from failurespot.data import annotation_budget
from failurespot.metrics import binary_auroc
from failurespot.selection import trajectory_uncertainty


def test_annotation_budget_is_global():
    assert annotation_budget(0.15, 3, 50) == 23


def test_uncertainty_averages_all_timestamps():
    probabilities = np.array([0.5, 0.01, 0.01, 0.01])
    expected = (
        -(probabilities * np.log(probabilities)
          + (1 - probabilities) * np.log(1 - probabilities))
    ).mean()
    assert np.isclose(trajectory_uncertainty(probabilities), expected)


def test_binary_auroc_perfect_and_ties():
    assert binary_auroc([0, 0, 1, 1], [0.1, 0.2, 0.8, 0.9]) == 1.0
    assert binary_auroc([0, 1], [0.5, 0.5]) == 0.5
