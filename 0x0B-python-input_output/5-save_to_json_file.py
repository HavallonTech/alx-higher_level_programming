#!/usr/bin/python3
"""
Module 5-save_to_json_file.py
a function that writes an Object to a text file,
using a JSON representation:
"""


def save_to_json_file(my_obj, filename):
    """Write a function that writes an object to a text file
       using Json representation
    """
    import json
    with open(filename, 'w', encoding="utf-8") as ff:
        json.dump(my_obj, ff)
