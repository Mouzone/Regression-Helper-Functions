import numpy as np
from mypkg.functions import is_same_length, is_not_zero


def test_is_same_length():
    # Test case where lengths are the same
    y_true = np.array([1, 2, 3])
    y_predict = np.array([4, 5, 6])
    assert is_same_length(y_true, y_predict) is True

    # Test case where lengths are different
    y_true = np.array([1, 2, 3])
    y_predict = np.array([4, 5])
    assert is_same_length(y_true, y_predict) is False


def test_is_not_zero():
    # Test case where the array is not empty
    y_true = np.array([1, 2, 3])
    assert is_not_zero(y_true) is True

    # Test case where the array is empty
    y_true = np.array([])
    assert is_not_zero(y_true) is False
