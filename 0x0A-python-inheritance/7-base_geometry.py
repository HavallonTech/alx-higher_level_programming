#!/usr/bin/python3
"""
Module for 7-base_geometry.py
"""


class BaseGeometry:
    """class methods comes after this line"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.value = value
        self.name = name
        if (not isinstance(self.value, int)):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
        
