class Interval(object):
    # A constructor of Interval class which creates a new list.
    def __init__(self):
        self.list = []

    """ The add method adds a new Tuple with given inputs to the list.
    
    Parameters
    ----------
    start : int
        first element of Tuple.
    end : int   
        second element of Tuple.
    """
    def add(self, start, end):
        self.list.append((start, end))

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
    def getFirst(self, index):
        return self.list[index][0]

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
    def getLast(self, index):
        return self.list[index][1]

    """ The size method returns the size of the list list.
    Returns
    ----------
    int
        size of the list list.
    """
    def size(self):
        return len(self.list)