import numpy as np


def is_same_length(y_true, y_predict):
    """Check if the inputs are valid for accuracy_score calculation."""
    if y_true.shape != y_predict.shape:
        return False
    return True


def is_not_zero(y_true):
    if y_true.size == 0:
        return False
    return True


def accuracy_score(y_true, y_predict):
    """
    Calculate accuracy score based on true positive, true negative,
    false positive, and false negative predictions.
    """
    if not is_same_length(y_true, y_predict):
        raise ValueError(f"Mismatch in shapes: {y_true.shape} and {y_predict.shape}")

    if not is_not_zero(y_true):
        raise ValueError("Input arrays must not be empty")

    true_pos = np.sum((y_true == y_predict) & (y_true == 1))
    true_neg = np.sum((y_true == y_predict) & (y_true == 0))
    false_pos = np.sum((y_true != y_predict) & (y_true == 0))
    false_neg = np.sum((y_true != y_predict) & (y_true == 1))

    denominator = true_neg + true_pos + false_neg + false_pos

    return (true_neg + true_pos) / denominator


def recall_score(y_true, y_predict):
    # TP/TP+FN
    """
    Calculate recall score based on true positive,
    and false negative predictions.
    """
    if not is_same_length(y_true, y_predict):
        raise ValueError(f"Mismatch in shapes: {y_true.shape} and {y_predict.shape}")

    if not is_not_zero(y_true):
        raise ValueError("Input arrays must not be empty")

    true_pos = np.sum((y_true == y_predict) & (y_true == 1))
    false_pos = np.sum((y_true != y_predict) & (y_true == 0))

    denominator = true_pos + false_pos

    return true_pos / denominator


def precision_score(y_true, y_predict):
    # TP/TP+FP
    return


def f1_score(y_true, y_predict):
    # 2*Precision*Recall/(Precision+Recall)
    return


def train_test_split(x, y):
    return
