#!/usr/bin/python3
"""
Module for 2-append_write.py
a function that appends a string to a text file (UTF8)
and returns the number of characters written:
"""


def append_write(filename="", text=""):
    strlen = filename
    """ The function to read from a file """
    with open(filename, 'a', encoding='utf-8') as ff:
        return(ff.write(text))
