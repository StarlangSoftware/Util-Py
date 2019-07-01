class Swap:

    """ The swap method takes a list and two integer numbers i, j. And interchange the given array's
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
    def swap(self, array, i, j):
        t = array[i]
        array[i] = array[j]
        array[j] = t
