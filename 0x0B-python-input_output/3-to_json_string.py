#!/usr/bin/python3
"""
Module for 3-to_json_string.py
a function to return object representation of a Json Object
"""


def to_json_string(my_obj):
    """Write a function that returns the JSON
       representation of an object (string):
    """
    import json
    return json.dumps(my_obj)
