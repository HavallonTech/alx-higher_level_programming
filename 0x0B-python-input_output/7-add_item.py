#!/usr/bin/python3
"""
Module for 7-add_item.py
Write a script that adds all arguments to a Python list
and then save them to a file:
"""


import os
import json
form sys import argv
save_to_json_file = __import__('5-save_to_json_file.py').save_to_json_file
load_from_json_file = \
    __import__('6-load_from_json_file.py').load_from_json_file
try:
    existing_data_item = load_from_json_file("add_item.json")
    combined_data = existing_data_item + argv[1:]

except FileNotFoundError:
    # If the file doesn't exist, create an empty list
    combined_data = []
    combined_data = argv[1:]
save_to_json_file(combined_data, "add_item.json")
