import numpy as np
from mypkg.functions import accuracy_score, recall_score


def test_accuracy_score():
    # Test case for accurate predictions
    y_true = np.array([1, 1, 0, 0, 1])
    y_predict = np.array([1, 1, 0, 0, 1])
    result = accuracy_score(y_true, y_predict)
    assert result == 1.0

    # Test case for mismatched lengths
    y_true = np.array([1, 0, 1])
    y_predict = np.array([0, 1])
    try:
        accuracy_score(y_true, y_predict)
    except ValueError as e:
        assert str(e) == "Mismatch in shapes: (3,) and (2,)"


def test_recall_score():
    # Test case for accurate predictions
    y_true = np.array([1, 1, 0, 0, 1])
    y_predict = np.array([1, 1, 0, 0, 1])
    result = recall_score(y_true, y_predict)
    assert result == 1.0

    # Test case for mismatched lengths
    y_true = np.array([1, 0, 1])
    y_predict = np.array([0, 1])
    try:
        recall_score(y_true, y_predict)
    except ValueError as e:
        assert str(e) == "Mismatch in shapes: (3,) and (2,)"