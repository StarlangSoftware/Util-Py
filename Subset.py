class Subset(object):

    """
    The constructor of Subset class which takes 3 integer inputs; rangeStart, rangeEnd, and elementCount.
    It initializes variables rangeEnd and elementCount with given inputs, creates 2 arrays; set and multiset with the
    size of given elementCount and multisetCount, which is derived from elementCount, respectively. Then, it assigns
    rangeStart+i to each ith element of set.

    Parameters
    ----------
    rangeStart : int
        input defining start range.
    rangeEnd : int
        input defining ending range.
    elementCount : int
        input element count.
    """
    def __init__(self, rangeStart: int, rangeEnd: int, elementCount: int):
        self.rangeEnd = rangeEnd
        self.elementCount = elementCount
        self.set = []
        self.multiset = []
        for i in range(elementCount):
            self.set.append(rangeStart + i)

    """
    Getter for the set list
    
    Returns
    ----------
    list
        the set list
    """
    def get(self) -> list:
        return self.set

    """
    The getX method takes an integer M as an input. Creates a new list X size of elementCount+2 and assigns 0 to its
    first element. Starting from the second index, it assigns set lists elements to newly
    created list X. Then, assigns M to the last element of X.
    
    Parameters
    ----------
    M
        integer input.
        
    Returns
    ----------
    list
        list of size of elementCount + 2.
    """
    def getX(self, M: int) -> list:
        X = []
        X.append(0)
        for i in range(self.elementCount):
            X.append(self.set[i])
        X.append(M)
        return X

    """
    Getter for the multiset list.

    Returns
    ----------
    list
        the multiset list.
    """
    def getmultiset(self) -> list:
        return self.multiset

    """
    The multiset method takes an integer M as an input. Assigns ith element of set list to even numbered
    indices of multiset list and M - ith element of set list to odd numbered
    indices of multiset list, and i is between 0 and elementCount. Then, assigns M to jth index of multiset
    list. At the end, fill up the rest of the multiset list via different
    indices of set list and sort the multiset list.
    
    Parameters
    ----------
    M
        integer input.
    """
    def multiset(self, M: int):
        for i in range(self.elementCount):
            self.multiset.append(self.set[i])
            self.multiset.append(M - self.set[i])
        self.multiset.append(M)
        for i in range(self.elementCount - 1, 0, -1):
            for k in range(i - 1, -1, -1):
                self.multiset.append(self.set[i] - self.set[k])
        self.multiset.sort()

    """
    The next method generates the next subset.

    Returns
    ----------
    boolean
        true if next subset generation is possible, false otherwise.
    """
    def next(self) -> bool:
        for i in range(self.elementCount - 1, -1, -1):
            self.set[i] = self.set[i] + 1
            if self.set[i] <= self.rangeEnd - self.elementCount + i + 1:
                break
        else:
            return False
        for j in range(i + 1, self.elementCount):
            self.set[j] = self.set[j - 1] + 1
        return True

    """
    The print method prints elements of set list.
    """
    def print(self):
        for i in range(self.elementCount):
            print(self.set[i], end=" ")
        print()
