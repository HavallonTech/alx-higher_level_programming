#!/usr/bin/python3

"""A module that defines the Rectangle Class python"""


class Rectangle:
    """A rectangle class with height and width"""
    def __init__(self, width=0, height=0):
        """A method that instantiates private attributes"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError('width must be >= 0')
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError('height must be >= 0')
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
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

    def area(self):
        """Returns the area of a square"""
        return self.width * self.height

    def perimeter(self):
        if self.height == 0 or self.width == 0:
            return 0
        """Returns the perimeter of a rectangle"""
        return 2 * (self.height + self.width)

    def __str__(self):
        """Returns a '#' symbol"""
        if (self.__width == 0 or self.__height == 0):
            return ("")
        final = []
        for i in range(self.__height):
            [final.append('#') for j in range(self.__width)]
            if i != (self.__height - 1):
                final.append('\n')
        return ("".join(final))
