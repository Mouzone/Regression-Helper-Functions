import numpy as np
#y_predict and y_true is numpy array
def accuracy_score(y_true, y_predict):
    #TP + TN/TP+TN+FP+FN
    #TP is when both are 1
    #TN is when both are 0
    #FP is when y_true is 0 and y_predict is 1
    #FN is when y_true is 1 and y_predict is 0
    return
def recall_score(y_true, y_predict):
    #TP/TP+FN
    return
def precision_score(y_true, y_predict):
    #TP/TP+FP
    return
def f1_score(y_true, y_predict):
    #2*Precision*Recall/(Precision+Recall)
    return
def train_test_split(x, y):
    return
