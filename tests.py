# test_my_module.py

import unittest
from my_module import add_numbers

class TestAddNumbersFunction(unittest.TestCase):
    def test_add_numbers_positive_numbers(self):
        result = add_numbers(3, 5)
        self.assertEqual(result, 8)

    def test_add_numbers_negative_numbers(self):
        result = add_numbers(-2, -4)
        self.assertEqual(result, -6)

    def test_add_numbers_mixed_numbers(self):
        result = add_numbers(10, -7)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()
