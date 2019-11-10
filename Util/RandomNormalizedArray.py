import random


class RandomNormalizedArray(object):

    __array: list

    """
    The constructor of RandomNormalizedArray class gets an integer itemCount as an input. Creates a list of
    size itemCount and loops through each element of the list and initializes them with a random number by using random.
    Then, accumulates each element of the list and at the end divides each element with the resulting sum.

    Parameters
    ----------
    itemCount : int
        input defining array size.
     """
    def __init__(self, itemCount: int):
        sum = 0.0
        self.__array = []
        for i in range(itemCount):
            self.__array.append(random.uniform(0, 1))
            sum += self.__array[i]
        for i in range(itemCount):
            self.__array[i] /= sum

    """
    Getter for the double list.
   
    Returns
    ----------
    list
        the double list.
     """
    def get(self) -> list:
        return self.__array