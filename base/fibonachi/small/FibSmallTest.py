import unittest
from FibSmall import fib

class SmallFibTestCase(unittest.TestCase):

    def test_test_first_three_fib_number(self):
        self.assertEqual(fib(1), 1, 'should be 1')
        self.assertEqual(fib(2), 1, 'should be 1')
        self.assertEqual(fib(3), 2, 'should be 2')
        self.assertEqual(fib(4), 3, 'should be 3')
        self.assertEqual(fib(5), 5, 'should be 5')

if __name__ == '__main__':
    unittest.main()

