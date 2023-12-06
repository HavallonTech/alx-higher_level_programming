#!/usr/bin/python3
"""
6-load_from_json_file.py
a function to create a object from a json file
"""


def load_from_json_file(filename):
    """Write a function that creats an object from a json file
    """
    import json
    with open(filename, 'r', encoding="utf-8") as ff:
        obj_created = json.load(ff)
    return (obj_created)
