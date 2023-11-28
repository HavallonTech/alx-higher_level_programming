#!/usr/bin/python3
"""
A module contains a function that prints my name
"""


def say_my_name(first_name, last_name=""):
    """"
    function that prints my fullname.

    Args:
        first_name: First name as string passed to the function
        last_name: String of lastname passed to the function

    Raises:
        TypeError:
           first_name must be a string
           last_name must be a string

    Returns:
        formated string saying my fullname
    """

    if (not isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    if (not isinstance(last_name, str)):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

if __name__ == "__main__":
    say_my_name("Messi")
