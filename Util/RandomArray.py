import random


class RandomArray(object):

    @staticmethod
    def normalizedArray(item_count: int) -> list:
        """
        The constructor of RandomNormalizedArray class gets an integer itemCount as an input. Creates a list of
        size itemCount and loops through each element of the list and initializes them with a random number by using
        random. Then, accumulates each element of the list and at the end divides each element with the resulting sum.

        Parameters
        ----------
        item_count : int
            input defining array size.
        """
        total = 0.0
        array = []
        for i in range(item_count):
            array.append(random.uniform(0, 1))
            total += array[i]
        for i in range(item_count):
            array[i] /= total
        return array

    @staticmethod
    def indexArray(item_count: int, seed: int) -> list:
        """
        Returns an array of array indexes but shuffled. For example, if n is 4, the method returns an array of indexes
        0, 1, 2, 3 but shuffled.

        Parameters
        ----------
        item_count: int
            Number of elements in the array
        seed: int
            Seed used to shuffle array.

        Returns
        ----------
        list
            Index array
        """
        array = [i for i in range(item_count)]
        random.seed(seed)
        random.shuffle(array)
        return array
