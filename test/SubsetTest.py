import unittest
from unittest import TestCase
from Util.Subset import Subset


class SubsetTest(TestCase):

    def test_next1(self):
        subSet = Subset(1, 10, 5)
        firstSubSet = subSet.get()
        self.assertEqual([1, 2, 3, 4, 5], firstSubSet)
        count = 1
        while subSet.next():
            count = count + 1
        self.assertEqual(252, count)

    def test_next2(self):
        subSet = Subset(1, 20, 3)
        firstSubSet = subSet.get()
        self.assertEqual([1, 2, 3], firstSubSet)
        count = 1
        while subSet.next():
            count = count + 1
        self.assertEqual(1140, count)

    def test_next3(self):
        count = 0
        for i in range(11):
            subSet = Subset(1, 10, i)
            count = count + 1
            while subSet.next():
                count = count + 1
        self.assertEqual(1024, count)


if __name__ == '__main__':
    unittest.main()