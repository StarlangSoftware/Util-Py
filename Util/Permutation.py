from Util.Swap import Swap


class Permutation(object):

    __a: list
    __n: int
    
    def __init__(self, n: int):
        """
        A constructor of Permutation class which creates a new list and assigns integer
        numbers starting from 0 to given input n.

        Parameters
        ----------
         n: int
            integer input.
         """
        self.__n = n
        self.__a = []
        for i in range(n):
            self.__a.append(i)

    def get(self) -> list:
        """
        The get method returns the list a.

        Returns
        ----------
        list
            a
        """
        return self.__a

    def next(self) -> bool:
        """
         The next method generates next permutation for the list a.

        Returns
        ----------
        boolean
            true if next permutation is possible, false otherwise.
        """
        i = self.__n - 2
        while i >= 0 and self.__a[i] >= self.__a[i + 1]:
            i = i - 1
        if i == -1:
            return False
        j = self.__n - 1
        while self.__a[i] >= self.__a[j]:
            j = j - 1
        Swap.swap(self.__a, i, j)
        k = i + 1
        j = self.__n - 1
        while k < j:
            Swap.swap(self.__a, j, k)
            k = k + 1
            j = j - 1
        return True
