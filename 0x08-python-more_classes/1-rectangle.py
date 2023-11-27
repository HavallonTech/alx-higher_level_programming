#!/usr/bin/python3

"""A module that defines a rectangle"""


class Rectangle:
    """A class that has a rectangle defined"""
    def __init__(self, width, height):
        if (not isinstance(width, int)):
            raise TypeError("width must be an integer")
        if (not isinstance(height, int)):
            raise TypeError("heigth must be an integer")
        if (width < 0):
            raise ValueError("width ,ust be >= 0")
        if (height < 0):
            raise ValueError("height must be >=0")
        self.height = height
        self.width = width

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if not (isinstance(value, int)):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
