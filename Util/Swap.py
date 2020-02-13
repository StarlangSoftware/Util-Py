class Swap(object):

    @staticmethod
    def swap(array: list, i: int, j: int):
        """
        The swap method takes a list and two integer numbers i, j. And interchange the given array's
        items at index i and index j.

        Parameters
        ----------
        array : list
            input
        i : int
            first index to swap.
        j : int
            second index to change.
        """
        t = array[i]
        array[i] = array[j]
        array[j] = t
