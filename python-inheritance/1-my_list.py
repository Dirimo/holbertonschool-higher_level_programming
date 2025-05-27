#!/usr/bin/python3
class MyList(list):
    """
    A class that inherits from list and provides a method to print the list in sorted order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.  Assumes all elements are integers.
        """
        print(sorted(self))

if __name__ == '__main__':
    # Example usage (not required for the tests, but good for demonstration)
    my_list = MyList([1, 4, 2, 3])
    print("Original list:", my_list)
    my_list.print_sorted()
