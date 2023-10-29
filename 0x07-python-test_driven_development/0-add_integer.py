#!/usr/bin/python3
""" a function to add two integers a and b using ALX craterias"""

def add_integer(a, b=98):

    """
    add_integer: function that adds two numbers (interger or float)

    Args:
        a: The first number to add
        b: The second number to add

    Returns:
        Return the sum of a and b which must be an integer

    Example:
        >>>> add_integer(6, 3)
        will return 9
    """
    if (not(isinstance(a, (int, float)))):
        raise TypeError("a must be an integer")
    elif (not (isinstance(b, (int, float)))):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
