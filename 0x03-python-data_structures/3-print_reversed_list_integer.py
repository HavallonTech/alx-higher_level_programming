#!/usr/bin/python3
# 3-print_reversed_list_integer.py


def print_reversed_list_integer(my_list=[]):
    """Print all integers of a list in reverse order."""
    k = len(my_list)
    s = k - 1
    for i in range(len(my_list)):
        if (s >= 0):
            print("{:d}".format(my_list[(s-k)]))
            s = s - 1
