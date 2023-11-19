# test_functions.py

import unittest
import numpy as np
from main import check_valid_inputs, accuracy_score  # Replace 'your_module' with the actual module name

class TestCheckValidInputsFunction(unittest.TestCase):
    def test_check_valid_inputs_valid_input(self):
        first = np.array([1, 2, 3])
        second = np.array([4, 5, 6])
        self.assertIsNone(check_valid_inputs(first, second))

    def test_check_valid_inputs_mismatched_lengths(self):
        first = np.array([1, 2, 3])
        second = np.array([4, 5])
        with self.assertRaises(ValueError) as context:
            check_valid_inputs(first, second)
        self.assertEqual(str(context.exception), "Mismatch in lengths 3 and 2")

    def test_check_valid_inputs_empty_input(self):
        first = np.array([])
        second = np.array([])
        with self.assertRaises(ValueError) as context:
            check_valid_inputs(first, second)
        self.assertEqual(str(context.exception), "No elements")

class TestAccuracyScoreFunction(unittest.TestCase):
    def test_accuracy_score_all_correct(self):
        y_true = np.array([1, 1, 0, 0, 1])
        y_predict = np.array([1, 1, 0, 0, 1])
        result = accuracy_score(y_true, y_predict)
        self.assertEqual(result, 1.0)

    def test_accuracy_score_all_incorrect(self):
        y_true = np.array([1, 1, 0, 0, 1])
        y_predict = np.array([0, 0, 1, 1, 0])
        result = accuracy_score(y_true, y_predict)
        self.assertEqual(result, 0.0)

    def test_accuracy_score_mixed_predictions(self):
        y_true = np.array([1, 1, 0, 0, 1])
        y_predict = np.array([1, 0, 1, 0, 1])
        result = accuracy_score(y_true, y_predict)
        self.assertEqual(result, 0.6)

    def test_accuracy_score_empty_input(self):
        y_true = np.array([])
        y_predict = np.array([])
        self.assertIsNone(accuracy_score(y_true, y_predict))

    def test_accuracy_score_unequal_lengths(self):
        y_true = np.array([1, 0, 1])
        y_predict = np.array([0, 1])
        with self.assertRaises(ValueError) as context:
            accuracy_score(y_true, y_predict)
        self.assertEqual(str(context.exception), "Mismatch in lengths 3 and 2")

if __name__ == '__main__':
    unittest.main()
