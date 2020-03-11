import unittest
from Util.Interval import Interval
from Util.Permutation import Permutation
from Util.SubsetFromList import SubsetFromList
from Util.RandomNormalizedArray import RandomNormalizedArray
from Util.Swap import Swap


class MyTestCase(unittest.TestCase):
    def test_interval(self):
        """ Creating Interval Object
            Adding two tuples separately.
        """
        interval = Interval()
        interval.add(0, 4)
        interval.add(1, 6)
        # Output : interval[0]'s first element calling .getFirst() function.
        print("First element on index 0 :" + repr(interval.getFirst(0)))
        # Output : interval[1]'s last element calling .getLast() function.
        print("Last element of index 1 :" + repr(interval.getLast(1)))
        # Output : Size of interval_list calling .size() function.
        print("Size of Interval List :" + repr(interval.size()))

    def test_permutation(self):
        """ Creating Permutation Object.
            Permutation creates list  0 to given integer.
            Adding two tuples separately.
        """
        permutation = Permutation(3)
        # Output created list.
        print("Created List :" + repr(permutation.get()))
        # All permutations of array.
        print("All Permitations:")
        while permutation.next() is not False:
            permutation.next()
            print(permutation.get())

    def test_SubsetFromList(self):
        # Creates subsets from given integer array with given element count which in this case is 2.
        _list = [5, 3, 2, 9]
        subSetFromList = SubsetFromList(_list, 2)
        # Using .next() will create new subsets.
        # Output
        print("Subsets of " + repr(_list) + " are:")
        while subSetFromList.next() is not False:
            subSetFromList.next()
            print(subSetFromList.get())

    def test_swap(self):
        """
        Swap takes a list and two integer numbers i, j. And interchange the given array's
        items at index i and index j.
        """
        swap = Swap()
        _array = [1, 2, 3, 4, 5]
        print("List: " + repr(_array))
        # _array[0] and _array[1] swapped.
        swap.swap(_array,0,1)
        print("Swapped List: "+repr(_array))


    def test_RandomNormalizedArray(self):
        """Object creates an array of size itemCount and loops through each element of the array ,
       and initializes them with a random number, at the end each array element divided to sum.
       """
        randomNormalizedArray = RandomNormalizedArray(4)
        # Output Generated list
        print("Generated List: "+repr(randomNormalizedArray.get()))


if __name__ == '__main__':
    unittest.main()
