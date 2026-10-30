import numpy as np

from failurespot.signals import compute_action_signals, exponential_moving_average


def test_ema_beta_point_eight():
    values = exponential_moving_average(np.array([0.0, 1.0, 1.0]), 0.8)
    np.testing.assert_allclose(values, [0.0, 0.2, 0.36], atol=1e-6)


def test_autoregressive_consistency():
    chunks = np.zeros((3, 1, 7), dtype=np.float32)
    chunks[1, 0, 0] = 1.0
    chunks[2, 0, 0] = 3.0
    signals = compute_action_signals(chunks, execution_horizon=1)
    np.testing.assert_allclose(signals.consistency, [0.0, 1.0, 2.0])


def test_chunk_overlap_uses_previous_unexecuted_actions():
    chunks = np.zeros((2, 4, 7), dtype=np.float32)
    chunks[0, 2:4, 0] = [1.0, 2.0]
    chunks[1, 0:2, 0] = [1.0, 4.0]
    signals = compute_action_signals(chunks, execution_horizon=2)
    assert signals.consistency[1] == 1.0
