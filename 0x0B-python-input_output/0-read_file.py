#!/usr/bin/python3
"""
Module for 0-read_file.py
"""


def read_file(filename=""):
    """
      The function to read from a file
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)
    except Exception as e:
        print(f"Error: {e}")
