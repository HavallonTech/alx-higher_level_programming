#!/usr/bin/python3
""" the main module for square.py
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Square class inheriting  from the Rectangle class
        Args: 
            Rectangle: Theis class inherits from the Rectangle
            class
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
            Retrieve the size of the rectangle
            Return:
                Returns the setted value for the size
                whivh is leght and breadth
        """
        return self.width

    @size.setter
    def size(self, value):
        """
            Set the value of the width
            Args:
                value which is the size of the square
        """
        self.width = value
        self.height = value



    def to_dictionary(self):
        """
            return the dictionary representaion of the Square
            Return: Returns the dictionary representation of
            the square
        """
        dictionary = {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
                }
        return dictionary

    def __str__(self):
        """
            str method
            return: 
                dormatted dictionary
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.width)