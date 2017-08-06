import unittest

from InsertSort import InsertSort


class InsertSortCase(unittest.TestCase):
    def test_array_sort(self):
        array = [6, 9, 1, 3, 7, 5, 4, 2, 8]

        InsertSort.sort(array)
        expected = range(1, len(array) + 1)
        print "Array = {}, expected = {}".format(array, expected)
        self.assertTrue(expected == array, "should be sorted")


if __name__ == '__main__':
    unittest.main()
