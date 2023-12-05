#!/usr/bin/python3
"""
Module for 4-inherits_from.py
"""


def inherits_from(obj, a_class):
    """
    a function that returns True if the object is an instance
    of a class that inherited (directly or indirectly) from the
    specified class ; otherwise False.
    Argument:
           obj
           a_class
    Return:
           True  or flase
    """
    return ((issubclass(type(obj), a_class)) and (type(obj) is not a_class))
