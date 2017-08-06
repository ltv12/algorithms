import unittest
from FibBig import fib_digit

class FibonachiLastDigitTestCase(unittest.TestCase):

    def test_test_first_three_fib_number(self):
        # 1 = 1
        # 2 = 1
        # 3 = 2
        # 4 = 3
        # 5 = 5
        self.assertEqual(fib_digit(6), 8, 'should be 8 for 8')
        self.assertEqual(fib_digit(7), 3, 'should be 3 for 13')
        self.assertEqual(fib_digit(8), 1, 'should be 1 for 21')
        self.assertEqual(fib_digit(9), 4, 'should be 1 for 34')

if __name__ == '__main__':
    unittest.main()

