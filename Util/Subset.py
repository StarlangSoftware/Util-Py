class Subset(object):

    set: list
    __range_end: int
    element_count: int

    def __init__(self, range_start: int, range_end: int, element_count: int):
        """
        The constructor of Subset class which takes 3 integer inputs; rangeStart, rangeEnd, and elementCount.
        It initializes variables rangeEnd and elementCount with given inputs, creates 2 arrays; set and multiset with
        the size of given elementCount and multisetCount, which is derived from elementCount, respectively. Then, it
        assigns rangeStart+i to each ith element of set.

        Parameters
        ----------
        range_start : int
            input defining start range.
        range_end : int
            input defining ending range.
        element_count : int
            input element count.
        """
        self.__range_end = range_end
        self.element_count = element_count
        self.set = []
        for i in range(element_count):
            self.set.append(range_start + i)

    def get(self) -> list:
        """
        Getter for the set list

        Returns
        ----------
        list
            the set list
        """
        return self.set

    def next(self) -> bool:
        """
        The next method generates the next subset.

        Returns
        ----------
        boolean
            true if next subset generation is possible, false otherwise.
        """
        for i in range(self.element_count - 1, -1, -1):
            self.set[i] = self.set[i] + 1
            if self.set[i] <= self.__range_end - self.element_count + i + 1:
                break
        else:
            return False
        for j in range(i + 1, self.element_count):
            self.set[j] = self.set[j - 1] + 1
        return True

    def __repr__(self):
        return f"{self.set}"
