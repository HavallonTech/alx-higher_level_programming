#!/usr/bin/python3
"""
Module for 12-pascal_triangle.py
"""

def pascal(num):
    pascal_list = []
    if num == 1:
        row = [1]
        pascal_list.append(row)
        return pascal_list
    else:
        result = pascal(num - 1) + pascal(num - 2)
        return result


def pascal_triangle(n):
    i = 1
    my_list = []
    if (n <= 0):
        return (my_list)
    else:
           
