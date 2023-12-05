#!/usr/bin/python3
"""
Module Exarct same object
"""


def is_same_class(obj, a_class):
    """A function that returns true if the exert same
     object is passed
    """
    myvalue = isinstance(obj, a_class)
    if myvalue:
        return (myvalue)
