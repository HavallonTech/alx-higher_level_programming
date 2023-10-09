#!/usr/bin/python3
# 8-multiple_returns.py


def multiple_returns(string):
    """Returns the length of a string and its first character."""
    if string == "":
        return (0, None)
    return (len(string), string[0])
