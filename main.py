import numpy as np


# helper functions
def check_valid_inputs(first, second):
    if len(first) != len(second):
        raise ValueError(f"Mismatch in lengths {len(first)} and {len(second)}")
    if len(first) == 0:
        raise ValueError(f"No elements")


# y_predict and y_true is numpy array
def accuracy_score(y_true, y_predict):
    try:
        check_valid_inputs(y_true, y_predict)
    except ValueError as e:
        print(f"Error: {e}")
        return None  # Or you can return a specific value indicating failure

    true_pos = 0
    true_neg = 0
    false_pos = 0
    false_neg = 0

    for i in range(len(y_true)):
        if y_true[i] == y_predict[i] == 0:
            true_neg += 1
        elif y_true[i] == y_predict[i] == 1:
            true_pos += 1
        elif y_true[i] == 1 and y_predict[i] == 0:
            false_neg += 1
        elif y_true[i] == 0 and y_predict[i] == 1:
            false_pos += 1

    return (true_neg + true_pos) / (true_neg + true_pos + false_neg + false_pos)


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
