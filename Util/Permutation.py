from Util.Swap import Swap


class Permutation(object):
    
    """
    A constructor of Permutation class which creates a new list and assigns integer
    numbers starting from 0 to given input n.

    Parameters
    ----------
     n: int
        integer input.
     """
    def __init__(self, n: int):
        self.n = n
        self.a = []
        for i in range(n):
            self.a.append(i)

    """
    The get method returns the list a.

    Returns
    ----------
    list 
        a
    """
    def get(self) -> list:
        return self.a

    """
     The next method generates next permutation for the list a.

    Returns
    ----------
    boolean
        true if next permutation is possible, false otherwise.
     """
    def next(self) -> bool:
        i = self.n - 2
        while i >= 0 and self.a[i] >= self.a[i + 1]:
            i = i - 1
        if i == -1:
            return False
        j = self.n - 1
        while self.a[i] >= self.a[j]:
            j = j - 1
        Swap.swap(self.a, i, j)
        k = i + 1
        j = self.n - 1
        while k < j:
            Swap.swap(self.a, j, k)
            k = k + 1
            j = j - 1
        return True