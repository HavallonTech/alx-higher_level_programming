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
        retlist = sorted(self)
        print(retlist)
