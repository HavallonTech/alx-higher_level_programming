#!/usr/bin/python3
"""
function that prints a square with the character #.
"""


def print_square(size):
    """
    print_square - prints a square with the character #.

    Args:
        size: The size of the square (int or float)

    Return: returns a squre with character #

    Example:
        >>> print_square(4)
        #####
        #####
        #####
        #####
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, (float)) < 0:
        raise TypeError("size must be an integer")
    i = 1
    while i <= size:
        for _ in range(size):
            print("#", end="")
        print()
        i = i + 1
