import unittest
from Util.Permutation import Permutation


class PermutationTest(unittest.TestCase):

    def test_next1(self):
        permutation = Permutation(3)
        firstPermutation = permutation.get()
        self.assertEqual([0, 1, 2], firstPermutation)
        count = 1
        while permutation.next():
            count = count + 1
        self.assertEqual(6, count)

    def test_next2(self):
        permutation = Permutation(5)
        firstPermutation = permutation.get()
        self.assertEqual([0, 1, 2, 3, 4], firstPermutation)
        count = 1
        while permutation.next():
            count = count + 1
        self.assertEqual(120, count)


if __name__ == '__main__':
    unittest.main()
