#!/usr/bin/python3
"""
Write a class Rectangle that defines a rectangle by:based on 7
"""


class Rectangle:
    """
    Class that define an empty rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialization of the class
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        static method that compare two rectangle
        Args:
            -rect_1(Rectangle): rectangle 1
            -rect_2(Rectangle): rectangle 2
        Returns: the biggest rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2

    @property
    def width(self):
        """
        Retrieve the width of the rectangle
        Returns:
            -int: the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the value of the width
        Args:
            -value (int): value to set
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        Retrieve the height of the rectangle
        Returns:
            -int: the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        set the value of the heigth
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        Method that give the area of rectangle
        Returns:
            -int : the area
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Method that give the perimeter of the rectangle
        Returns:
            -int : the perimeter
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2

    def __str__(self):
        """
        Print the rectangle with #
        """
        if self.__height == 0 or self.__width == 0:
            return ""
        return ("\n".join("{}".format(self.print_symbol) * self.__width
                for _ in range(self.__height)))

    def __repr__(self):
        """
        Print specific info
        """
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """
        delete message
        """
        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1
