#!/usr/bin/python3
"""class Square that inherits from Rectangle (9-rectangle.py)"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ class square """
    def __init__(self, size):
        """ constructor for instantiation of size """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = sizei
