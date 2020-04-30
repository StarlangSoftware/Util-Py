from Util.Subset import Subset


class SubsetFromList(Subset):

    __elementList: list
    __indexList: list

    def __init__(self, _list: list, elementCount: int):
        """
        A constructor of SubsetFromList class takes an integer list and an integer elementCount as inputs. It
        initializes elementList and elementCount variables with given inputs, then creates 3 arrays; set,indexList, and
        multiset with the size of given elementCount and multisetCount, which is derived from elementCount,
        respectively. Then, it assigns i to each ith element of indexList list and use this index to point at
        elementList and assigns to set list.

        Parameters
        ----------
        _list : list
            list type input.
        elementCount : int
            input element count.
        """
        self.__elementList = _list
        self.elementCount = elementCount
        self.set = []
        self.__indexList = []
        for i in range(elementCount):
            self.__indexList.append(i)
            self.set.append(self.__elementList[self.__indexList[i]])

    def next(self) -> bool:
        """
        The next method generates the next subset from list.

        Returns
        ----------
        boolean
            true if next subset generation from list is possible, false otherwise.
        """
        for i in range(self.elementCount - 1, -1, -1):
            self.__indexList[i] = self.__indexList[i] + 1
            if self.__indexList[i] < len(self.__elementList) - self.elementCount + i + 1:
                break
        else:
            return False
        self.set[i] = self.__elementList[self.__indexList[i]]
        for j in range(i + 1, self.elementCount):
            self.__indexList[j] = self.__indexList[j - 1] + 1
            self.set[j] = self.__elementList[self.__indexList[j]]
        return True
