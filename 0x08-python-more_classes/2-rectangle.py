#!/usr/bin/python3
"""
class Rectangle that defines a rectangle by: (based on 1-rectangle.py)
with applicaion of private and public instance attributes
"""


class Rectangle:
    """ A class rectangle
        Attributes:
                    Width : width of the rectangle which is an integer
                    height: height of the rectangle (integer)
        Methods:
                def area(self): public instance method to calculate the area
                def perimeter(self): public instance method to calculate the
                                    perimeter
    """
    def __init__(self, width=0, height=0):
        """ __init__ method to initialize the attributes of the class"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """ to retrieve width """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ to retrieve height """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the value of the height if all conditions are met """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """public attribute that returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """ calculates the perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
