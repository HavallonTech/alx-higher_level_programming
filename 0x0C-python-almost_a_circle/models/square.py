#!/usr/bin/python3
""" the main module for square.py
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class inheriting  from the Rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Retrieve the size of the rectangle
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the value of the width
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        method that assigns attributes
        """
        key = ["id", "size", "x", "y"]

        if args:
            for i, arg in enumerate(args):
                setattr(self,  key[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        return the dictionary representaion of the Square
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
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.width)
