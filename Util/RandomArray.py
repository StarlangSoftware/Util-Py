import random


class RandomArray(object):

    @staticmethod
    def normalizedArray(itemCount: int) -> list:
        """
        The constructor of RandomNormalizedArray class gets an integer itemCount as an input. Creates a list of
        size itemCount and loops through each element of the list and initializes them with a random number by using
        random. Then, accumulates each element of the list and at the end divides each element with the resulting sum.

        Parameters
        ----------
        itemCount : int
            input defining array size.
        """
        total = 0.0
        array = []
        for i in range(itemCount):
            array.append(random.uniform(0, 1))
            total += array[i]
        for i in range(itemCount):
            array[i] /= total
        return array

    @staticmethod
    def indexArray(itemCount: int, seed: int) -> list:
        array = [i for i in range(itemCount)]
        random.seed(seed)
        random.shuffle(array)
        return array
