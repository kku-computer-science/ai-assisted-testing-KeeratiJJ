import unittest
from sum_of_digits import get_sum_of_digits

class TestSumOfDigits(unittest.TestCase):
    def test_single_digit_number(self):
        self.assertEqual(get_sum_of_digits(5), 5)

    def test_multiple_digit_number(self):
        self.assertEqual(get_sum_of_digits(123), 6)

    def test_zero(self):
        self.assertEqual(get_sum_of_digits(0), 0)

    def test_negative_number(self):
        self.assertEqual(get_sum_of_digits(-123), 6)

if __name__ == '__main__':
    unittest.main() 