import numpy as np


# y_predict and y_true is numpy array
def accuracy_score(y_true, y_predict):
    # TP + TN/TP+TN+FP+FN
    # TP is when both are 1
    # TN is when both are 0
    # FP is when y_true is 0 and y_predict is 1
    # FN is when y_true is 1 and y_predict is 0
    true_pos = 0
    true_neg = 0
    false_pos = 0
    false_neg = 0
    if len(y_true) != len(y_predict):
        raise ValueError(f"Mismatch in lengths {len(y_true)} and {len(y_predict)}")
    if len(y_true) == 0:
        raise ValueError(f"No elements")
    for i in range(len(y_true)):
        if y_true[i] == y_predict[i] == 0:
            true_neg+=1
        elif y_true[i] == y_predict[i] == 1:
            true_pos+=1
        elif y_true == 1:
            false_neg += 1
        else:
            false_pos += 1
    
    return (true_neg + true_pos)/(true_neg+true_pos+false_neg+false_pos)


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
