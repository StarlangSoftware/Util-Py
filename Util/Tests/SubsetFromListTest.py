import unittest

from Util.SubsetFromList import SubsetFromList


class SubsetFromListTest(unittest.TestCase):

    def test_next1(self):
        subSet = SubsetFromList([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 5)
        firstSubSet = subSet.get()
        self.assertEqual([10, 20, 30, 40, 50], firstSubSet)
        count = 1
        while subSet.next():
            count = count + 1
        self.assertEqual(252, count)

    def test_next2(self):
        subSet = SubsetFromList([9, 8, 2, 12, 7, 16, 17], 3)
        firstSubSet = subSet.get()
        self.assertEqual([9, 8, 2], firstSubSet)
        count = 1
        while subSet.next():
            count = count + 1
        self.assertEqual(35, count)

    def test_next3(self):
        count = 0
        for i in range(10):
            subSet = SubsetFromList([9, 8, 2, 12, 7, 16, 17, 8, 3], i)
            count = count + 1
            while subSet.next():
                count = count + 1
        self.assertEqual(512, count)


if __name__ == '__main__':
    unittest.main()
