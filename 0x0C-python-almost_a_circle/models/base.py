#!/usr/bin/python3
"""
module for base.py
"""


class Base:
    """private class attribute """
    __nb_objects = 0

    def __init__(self, id=None):
        """Init method always called when an instance is raise
        """
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    """
    def draw(list_rectangles, list_squares):
        """
         the draw method
        """
        pass
        """
