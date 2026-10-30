import numpy as np

from failurespot.data import Trajectory, load_trajectory, validate_trajectories
from failurespot.smoke import smoke_config


def test_deviation_and_recovery_create_timestamp_labels(tmp_path):
    path = tmp_path / "trajectory.npz"
    np.savez(
        path,
        features=np.zeros((5, 3), dtype=np.float32),
        action_chunks=np.zeros((5, 1, 7), dtype=np.float32),
        trajectory_label=np.array(0),
        deviation_index=np.array(1),
        recovery_index=np.array(4),
        policy=np.array("openvla"),
        task_id=np.array(0),
        episode_id=np.array(2),
    )
    trajectory = load_trajectory(path)
    np.testing.assert_array_equal(trajectory.timestamp_labels, [0, 1, 1, 1, 0])


def test_protocol_validation_rejects_incomplete_corpus(tmp_path):
    config = smoke_config(tmp_path)
    trajectory = Trajectory(
        policy="smoke",
        task_id=0,
        episode_id=0,
        features=np.zeros((2, 4), dtype=np.float32),
        action_chunks=np.zeros((2, 1, 7), dtype=np.float32),
        timestamp_labels=np.zeros(2, dtype=np.float32),
        trajectory_label=0,
    )
    try:
        validate_trajectories([trajectory], config)
    except ValueError as error:
        assert "task IDs" in str(error)
    else:
        raise AssertionError("Invalid corpus should be rejected")
