#!/usr/bin/python3
""" A definintion of an empty class """


class Square:
    """A pass statement used to walk throug the class methods"""

    def __init__(self, size=0, position=(0, 0)):
        if (type(size)) != int:
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    def area(self):
        """area method declaration"""

        return (self.__size * self.__size)

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if (type(value)) != int:
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) and len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (not isinstance(value[0], int) or not isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        """ if (type(value)) == tuple and len(value) == 2 (value[0]) > 0 and \
        (value[1]) > 0 and(type(value[0]))==int and(type(value[1])) == int:"""

        self.__position = value

    def my_print(self):
        if (self.__size) == 0:
            print("")
        else:
            for a in range(self.position[1]):
                print("")
            for a in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
