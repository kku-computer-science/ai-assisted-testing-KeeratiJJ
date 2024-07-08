import unittest

def Sum_of_Digits(num):
    while num >= 10:
        num = sum(int(digit) for digit in str(num))
    return num

class TestSumOfDigits(unittest.TestCase):
    
    def test_single_digit(self):
        self.assertEqual(Sum_of_Digits(5), 5)
    
    def test_multiple_digits(self):
        self.assertEqual(Sum_of_Digits(123), 6)
        self.assertEqual(Sum_of_Digits(9875), 2)
        self.assertEqual(Sum_of_Digits(99999), 9)
    
    def test_large_number(self):
        self.assertEqual(Sum_of_Digits(123456789), 9)

if __name__ == '__main__':
    unittest.main()