import numpy as np


def check_valid_inputs(y_true, y_predict):
    """Check if the inputs are valid for accuracy_score calculation."""
    if y_true.shape != y_predict.shape:
        raise ValueError(f"Mismatch in shapes: {y_true.shape} and {y_predict.shape}")
    if y_true.size == 0:
        raise ValueError("Input arrays must not be empty")


def accuracy_score(y_true, y_predict):
    """
    Calculate accuracy score based on true positive, true negative,
    false positive, and false negative predictions.
    """
    try:
        check_valid_inputs(y_true, y_predict)
    except ValueError as e:
        print(f"Error: {e}")
        return None  # Or you can return a specific value indicating failure

    true_pos = np.sum((y_true == y_predict) & (y_true == 1))
    true_neg = np.sum((y_true == y_predict) & (y_true == 0))
    false_pos = np.sum((y_true != y_predict) & (y_true == 0))
    false_neg = np.sum((y_true != y_predict) & (y_true == 1))

    denominator = true_neg + true_pos + false_neg + false_pos

    return (true_neg + true_pos) / denominator if denominator != 0 else None


def recall_score(y_true, y_predict):
    # TP/TP+FN
    return


def precision_score(y_true, y_predict):
    # TP/TP+FP
    return


def f1_score(y_true, y_predict):
    # 2*Precision*Recall/(Precision+Recall)
    return


def train_test_split(x, y):
    return
