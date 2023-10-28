#!/usr/bin/python3
""" A definintion of an empty class """


class Square:
    """A pass statement used to walk throug the class methods"""

    def __init__(self, size=0):
        if (type(size)) != int:
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
