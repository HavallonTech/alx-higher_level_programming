#!/usr/bin/python3
# 8-uppercase.py


def uppercase(str):
    """Print a string in uppercase."""
    for k in str:
        if ord(k) >= 97 and ord(k) <= 122:
            k = chr(ord(k) - 32)
        print("{}".format(k), end="")
    print("")
