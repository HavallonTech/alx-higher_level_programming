#!/usr/bin/python3
"""
The 3-say_my_name module for printing name
"""


def say_my_name(first_name, last_name=""):
    """
    Function that prints My name is <first name> <last name>
    Args:
        -fist_name (str): first name
        -last_name (str): last name
    Raises:
        -TypeError: check for invalid input
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
