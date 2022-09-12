from Util.Subset import Subset


class SubsetFromList(Subset):

    __element_list: list
    __index_list: list

    def __init__(self, _list: list, element_count: int):
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
        element_count : int
            input element count.
        """
        self.__element_list = _list
        self.elementCount = element_count
        self.set = []
        self.__index_list = []
        for i in range(element_count):
            self.__index_list.append(i)
            self.set.append(self.__element_list[self.__index_list[i]])

    def next(self) -> bool:
        """
        The next method generates the next subset from list.

        Returns
        ----------
        boolean
            true if next subset generation from list is possible, false otherwise.
        """
        for i in range(self.elementCount - 1, -1, -1):
            self.__index_list[i] = self.__index_list[i] + 1
            if self.__index_list[i] < len(self.__element_list) - self.elementCount + i + 1:
                break
        else:
            return False
        self.set[i] = self.__element_list[self.__index_list[i]]
        for j in range(i + 1, self.elementCount):
            self.__index_list[j] = self.__index_list[j - 1] + 1
            self.set[j] = self.__element_list[self.__index_list[j]]
        return True
