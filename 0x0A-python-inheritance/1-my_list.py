#!/usr/bin/python3
"""
Module 1-my_list.py
"""


class MyList(list):
    """The class My list inherits from list
       which should be a supper class
    """
    def print_sorted(self):
        """
         Class method to print the list in sorted order
        """
        new_list = sorted(self)
        print(new_list)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
