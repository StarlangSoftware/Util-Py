class Interval(object):

    __list: list

    # A constructor of Interval class which creates a new list.
    def __init__(self):
        self.__list = []

    """ The add method adds a new Tuple with given inputs to the list.
    
    Parameters
    ----------
    start : int
        first element of Tuple.
    end : int   
        second element of Tuple.
    """
    def add(self, start: int, end: int):
        self.__list.append((start, end))

    """ The getFirst method returns the first element at the list list's given index.
    
    Parameters
    ----------
    index : int 
        to use at getting tuple from list.

    Returns
    ----------
    item
        the first element at the list list's given index.
    """
    def getFirst(self, index: int) -> int:
        return self.__list[index][0]

    """ The getLast method returns the last element at the list list's given index.

    Parameters
    ----------
    index : int 
        to use at getting tuple from list.

    Returns
    ----------
    item
        the last element at the list list's given index.
    """
    def getLast(self, index: int) -> int:
        return self.__list[index][1]

    """ The size method returns the size of the list list.
    Returns
    ----------
    int
        size of the list list.
    """
    def size(self) -> int:
        return len(self.__list)