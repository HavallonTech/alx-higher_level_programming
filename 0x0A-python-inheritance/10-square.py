#!/usr/bin/python3
"""class Square that inherits from Rectangle (9-rectangle.py)"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ class square """
    def __init__(self, size):
        """ constructor for instantiation of size """
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        return "[Rectangle]{:d}/{:d}".format(self.__size, self.__size)

    def area(self):
        return self.__size * self.__size
