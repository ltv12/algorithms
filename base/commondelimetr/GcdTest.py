import unittest

from Gcd import gcd


class GcdTest(unittest.TestCase):

    def test_evclid_gcd(self):
        self.assertEqual(gcd(4, 6), 2, "commond delimetr is 2")
        self.assertEqual(gcd(18, 35), 1, "commond delimetr is 1")
        self.assertEqual(gcd(14159572, 63967072), 4, "commond delimetr is 4")




if __name__ == '__main__':
    unittest.main()

