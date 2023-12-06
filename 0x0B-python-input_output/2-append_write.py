#!/usr/bin/python3
"""
Module for 2-append_write.py
a function that appends a string to a text file (UTF8)
and returns the number of characters written:
"""


def append_write(filename="", text=""):
    """ A  function that appends to a file """
    strlen = len(text)
    with open(filename, 'a', encoding='utf-8') as ff:
        ff.write(text)
    return (strlen)
