import unittest
from calc import add
class TestCalculator(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(add(2, 3), 5)
    def test_negative_number(self):
        self.assertEqual(add(-2, -3), -5)
    def test_positive_negative(self):
        self.assertEqual(add(6, -2), 4)
    def test_zero(self):
        self.assertEqual(add(0, 5), 5)
    def test_both_zero(self):
        self.assertEqual(add(0, 0), 0)
if __name__ == '__main__':
    unittest.main()