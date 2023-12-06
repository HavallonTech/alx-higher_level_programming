#!/usr/bin/python3
"""
Module for 4-from_json_string.py
te a function that returns an object (Python data structure)
represented by a JSON string:
"""


def from_json_string(my_str):

    """Write a function that returns JSON object of
     python data structure
    """
    import json
    return json.loads(my_str)
