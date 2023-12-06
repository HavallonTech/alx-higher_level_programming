#!/usr/bin/python3
"""
Module for 1-write_file.py
a function that writes a string to a text file (UTF8)
and returns the number of characters written:
"""


def write_file(filename="", text=""):
    """ The function to read from a file """
    strlen = len(text)
    with open(filename, 'w', encoding='utf-8') as ff:
        ff.write(text)
    return (strlen)
