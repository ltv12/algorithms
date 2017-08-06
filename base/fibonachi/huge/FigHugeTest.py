import unittest
from FibHuge import fib_mod

class HugeFibModTest(unittest.TestCase):

    def test_fib_number_n_mod_m(self):
        self.assertEqual(fib_mod(5, 2), 1, "expected 1 for 5%2")
        self.assertEqual(fib_mod(6, 4), 0, "expected 2 for 8%4")
        self.assertEqual(fib_mod(7, 5), 3, "expected 3 for 13%5")
        self.assertEqual(fib_mod(8, 6), 3, "expected 3 for 21%6")

if __name__ == '__main__':
    unittest.main()