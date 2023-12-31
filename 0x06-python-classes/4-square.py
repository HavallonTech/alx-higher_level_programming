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

    def area(self):
        """area method declaration"""

        return (self.__size * self.__size)

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if (type(value)) != int:
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value
