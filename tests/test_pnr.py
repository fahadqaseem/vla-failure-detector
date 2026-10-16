import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pnr.pnr import find_pnr, timeline_row, value_curve  # noqa: E402

CK = [0, 40, 80, 120, 160]


def test_pnr_first_point_of_final_bad_run():
    s = np.array([[1, 1, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0]])
    assert find_pnr(CK, s, min_fail=3) == 80


def test_pnr_must_stay_failing():
    # bad at 40, recovers at 80, bad again from 120: PNR is 120, not 40
    s = np.array([[1, 1, 1, 1, 1], [0, 0, 0, 1, 1], [1, 1, 1, 1, 0], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0]])
    assert find_pnr(CK, s, min_fail=3) == 120


def test_no_pnr_when_last_checkpoint_recoverable():
    s = np.array([[1] * 5, [1] * 5, [0] * 5, [0] * 5, [1, 1, 1, 0, 0]])
    assert find_pnr(CK, s, min_fail=3) is None


def test_doomed_from_start():
    assert find_pnr(CK, np.zeros((5, 5)), min_fail=3) == 0


def test_value_and_timeline():
    assert np.allclose(value_curve(np.array([[1, 0], [0, 0]])), [0.5, 0.0])
    row = timeline_row(160, 250, 295)
    assert row["detection_window"] == 90 and row["intervention_window"] == 135
    assert timeline_row(None, 250, None)["detection_window"] is None


def test_alarm_classes():
    from pnr.pnr import classify_alarm, value_at
    s = np.array([[1, 1, 1, 1, 1], [1, 1, 0, 1, 1], [0, 0, 0, 1, 0], [0] * 5, [0] * 5])
    assert value_at(CK, s, 95) == 0.2 and value_at(CK, s, -1) is None
    assert classify_alarm(50, 80, 150, 0.8, False) == "early"
    assert classify_alarm(100, 80, 150, 0.2, False) == "in_window"
    assert classify_alarm(170, 80, 150, 0.0, False) == "late"
    assert classify_alarm(100, None, None, None, True) == "unnecessary_stop"
