# Util-Py

For Developers
============
You can also see either [Java](https://github.com/olcaytaner/Util) 
or [C++](https://github.com/olcaytaner/Util-CPP) repository.
## Requirements

* [Python 3.7 or higher](#python)
* [Git](#git)

### Python 

To check if you have a compatible version of Python installed, use the following command:

    python -V
    
You can find the latest version of Python [here](https://www.python.org/downloads/).

### Git

Install the [latest version of Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

## Download Code

In order to work on code, create a fork from GitHub page. 
Use Git for cloning the code to your local or below line for Ubuntu:

	git clone <your-fork-git-link>

A directory called Util will be created. Or you can use below link for exploring the code:

	git clone https://github.com/olcaytaner/Util-Py.git

## Open project with Pycharm IDE

Steps for opening the cloned project:

* Start IDE
* Select **File | Open** from main menu
* Choose `Util-PY` file
* Select open as project option
* Couple of seconds, dependencies will be downloaded. 


## Compile

**From IDE**

After being done with the downloading and Maven indexing, select **Build Project** option from **Build** menu. After compilation process, user can run Util-Py.

### Examples


 * Interval
 
 	Creating an Interval and adding tuples with given integers First and Last respectively.
 	 
        interval = Interval()
        interval.add(0, 4)
        interval.add(1, 6)
	  
	Interval[0]'s first element calling .getFirst() function.
	
        print("First element on index 0 :" + repr(interval.getFirst(0)))
	
	Interval[1]'s last element calling .getLast() function.
	
        print("Last element of index 1 :" + repr(interval.getLast(1)))
	
	Size of interval_list calling .size() function.
	
        print("Size of Interval List :" + repr(interval.size()))
	   
	Output
	  
	   First element on index 0 :0
           Last element of index 1 :6
           Size of Interval List :2
	   
 * RandomNormalizedArray
 	
	Gets an integer itemCount as an input. Creates an array of size itemCount and loops through each element of the array         and initializes them with a random number, at the end each array element divided to sum.
	
	Creates a double array as a size of 3 and divide each element to sum.Using .get() method you can print the array elements.
	 
	   randomNormalizedArray = RandomNormalizedArray(4)
	   print("Generated List: "+repr(randomNormalizedArray.get()))
	   
	Output 
	
	   [0.2487524169259855, 0.30247636299454594, 0.22774359412166229, 0.22102762595780637]
	   
     
 * Permutation
 
 	Creates an integer array 0 to given input.By using .get() method we can get the generated array.
	
	    permutation = Permutation(3)
   	    print("Created List :" + repr(permutation.get()))
	   
	Output
	   
	   Created List :[0, 1, 2]

	 All permutations of array.
	   
	   print("All Permitations:")
	   while permutation.next() is not False:
            permutation.next()
            print(permutation.get())
	   
	 Output

	   All Permitations:
	   [1, 0, 2]
	   [2, 0, 1]	
	   [2, 1, 0]
	   
	   
 
  * SubsetFromList
         
	 Creates subsets from given integer array with given subset's element count.
	    
	    _list = [5, 3, 2, 9]
            subSetFromList = SubsetFromList(_list, 2)
	    SubsetFromList subsetFromList = new SubsetFromList(arrayList,3);
	 
	 Using .next() will create new subsets.
	  
	    print("Subsets of " + repr(_list) + " are:")
           while subSetFromList.next() is not False:
            subSetFromList.next()
            print(subSetFromList.get())
   	 
	 Output
	 
	    Subsets of [5, 3, 2, 9] are:
		[5, 9]
		[3, 9]
		
 * Swap
 
 	Swap takes a list and two integer numbers i, j. And interchange the given array's
        items at index i and index j.
	
	   swap = Swap()
           _array = [1, 2, 3, 4, 5]
            print("List: " + repr(_array))   
	 
          swap.swap(_array,0,1)
          print("Swapped List: "+repr(_array))
	  
	  _array[0] and _array[1] swapped.
	  
	  Output
	  
	   List: [1, 2, 3, 4, 5]
	   Swapped List: [2, 1, 3, 4, 5]
	   
	   
