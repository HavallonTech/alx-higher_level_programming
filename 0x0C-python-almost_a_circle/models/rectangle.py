#!/usr/bin/python3
"""
module for the rectangle class that inherits from the Base class
"""


from models.base import Base


class Rectangle(Base):
    """
     The clasee private attribute each with its own setter and getter
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
         Calling the super init method of the parent class
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        """ self.y and self.x calls the setter and
          getter method as if they were private attributes
        """
    def area(self):
        """public method of area, to calsulate area of a rectangle
        """
        return (self.height * self.width)

    def display(self):
        """ this method displays the rectangle using the # in place of the
            Area as calculated
            exp: y and x are used to add top and left marging before printint
        """
        space = " "
        a = self.height
        b = self.width
        i = 1
        j = 1
        while j <= self.y:
            print("")
            j += 1
        while i <= a:
            print(space * self.x, "#" * b)
            i += 1

    def update(self, *args, **kwargs):
        pass

    @property
    def y(self):
        return self.__y
    """ a setter method for protected y"""

    @y.setter
    def y(self, y):
        if (not isinstance(y, int)):
            raise TypeError("y must be an integer")
        if (y < 0):
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if (not isinstance(x, int)):
            raise TypeError("x must be an integer")
        if (x < 0):
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if (not isinstance(width, int)):
            raise TypeError("width must be an integer")
        if (width < 0):
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if (not isinstance(height, int)):
            raise TypeError("height must be an integer")
        if (height < 0):
            raise ValueError("height must be > 0")
        self.__height = height

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} -\
        {self.width}/{self.height}"
