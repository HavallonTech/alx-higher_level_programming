#!/usr/bin/python3
"""
Module for 0-read_file.py
"""


def read_file(filename=""):
    """
      The function to read from a file
    """
    with open(filename, 'r', encoding='utf-8') as ff:
        file_content = ff.read()
        print(file_content, end = ' ')
