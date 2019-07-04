import Subset


class SubsetFromList(Subset):

    """
    A constructor of SubsetFromList class takes an integer list and an integer elementCount as inputs. It initializes
    elementList and elementCount variables with given inputs, then creates 3 arrays; set,indexList, and multiset with the
    size of given elementCount and multisetCount, which is derived from elementCount, respectively. Then, it assigns
    i to each ith element of indexList list and use this index to point at elementList and
    assigns to set list.
    
    Parameters
    ----------
    list : list
        list type input.
    elementCount : int
        input element count.
    """
    def __init__(self, list, elementCount):
        self.elementList = list
        self.elementCount = elementCount
        self.set = []
        self.indexList = []
        self.multiset = []
        for i in range(elementCount):
            self.indexList.append(i)
            self.set.append(self.elementList[self.indexList[i]])


    """
    The next method generates the next subset from list.

    Returns
    ----------
    boolean
        true if next subset generation from list is possible, false otherwise.
    """
    def next(self):
        for i in range(self.elementCount - 1, -1, -1):
            self.indexList[i] = self.indexList[i] + 1
            if self.indexList[i] < len(self.elementList) - self.elementCount + i + 1:
                break
        else:
            return False
        self.set[i] = self.elementList[self.indexList[i]]
        for j in range(i + 1, self.elementCount):
            self.indexList[j] = self.indexList[j - 1] + 1
            self.set[j] = self.elementList[self.indexList[j]]
        return True