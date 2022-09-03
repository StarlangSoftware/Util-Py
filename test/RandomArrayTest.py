import unittest

from RandomArray import RandomArray


class RandomNormalizedArrayTest(unittest.TestCase):

    def test_normalized_array(self):
        array = RandomArray.normalizedArray(10)
        sum = 0.0
        for d in array:
            sum += d
        self.assertEqual(1.0, sum, 0.0000000001)

    def test_index_array(self):
        array = RandomArray.indexArray(10, 0)
        sum = 0
        for d in array:
            sum += d
        self.assertEqual(45, sum)


if __name__ == '__main__':
    unittest.main()
