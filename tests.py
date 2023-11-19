# test_accuracy_score.py

import unittest
from main import accuracy_score  # Replace 'your_module' with the actual module name

class TestAccuracyScoreFunction(unittest.TestCase):
    def test_accuracy_score_all_correct(self):
        y_true = [1, 1, 0, 0, 1]
        y_predict = [1, 1, 0, 0, 1]
        result = accuracy_score(y_true, y_predict)
        self.assertEqual(result, 1.0)

    def test_accuracy_score_all_incorrect(self):
        y_true = [1, 1, 0, 0, 1]
        y_predict = [0, 0, 1, 1, 0]
        result = accuracy_score(y_true, y_predict)
        self.assertEqual(result, 0.0)

    def test_accuracy_score_mixed_predictions(self):
        y_true = [1, 1, 0, 0, 1]
        y_predict = [1, 0, 1, 0, 1]
        result = accuracy_score(y_true, y_predict)
        self.assertEqual(result, 0.6)

    def test_accuracy_score_empty_input(self):
        y_true = []
        y_predict = []
        with self.assertRaises(ValueError) as context:
            accuracy_score(y_true, y_predict)
        self.assertEqual(str(context.exception), "No elements")

    def test_accuracy_score_unequal_lengths(self):
        y_true = [1, 0, 1]
        y_predict = [0, 1]
        with self.assertRaises(ValueError) as context:
            accuracy_score(y_true, y_predict)
        self.assertEqual(str(context.exception), "Mismatch in lengths 3 and 2")

if __name__ == '__main__':
    unittest.main()
