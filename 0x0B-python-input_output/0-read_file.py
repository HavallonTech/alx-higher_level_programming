#!/usr/bin/python3
"""
Module for 0-read_file.py
function that reads a text file (UTF8) and prints it to stdout:
"""


def read_file(filename=""):
    """ The function to read from a file """
    with open(filename, 'r', encoding='utf-8') as ff:
        file_content = ff.read()
        print(file_content, end="")
    ff.close()
