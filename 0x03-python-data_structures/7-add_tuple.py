#!/usr/bin/python3
# 7-add_tuple.py


def add_tuple(tuple_one=(), tuple_two=()):
    """Add two tuples."""
    if len(tuple_one) < 2:
        if len(tuple_one) == 0:
            tuple_one = 0, 0
        else:
            tuple_one = tuple_one[0], 0
    if len(tuple_two) < 2:
        if len(tuple_two) == 0:
            tuple_two = 0, 0
        else:
            tuple_two = tuple_two[0], 0

    return (tuple_one[0] + tuple_two[0], tuple_one[1] + tuple_two[1])
