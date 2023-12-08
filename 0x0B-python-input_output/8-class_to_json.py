#!/usr/bin/python3
"""
Module for 8-class_to_json.pyi
Write a function that returns the dictionary description with
simple data structure (list, dictionary, string, integer and
boolean) for JSON serialization of an object:
"""


def class_to_json(obj):

    """
      function to return a dictionary description of obj
    """
    return obj.__dict__
