#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dir = a_dictionary.copy()
    list_keys = list(new_dir.keys())

    for z in list_keys:
        new_dir[z] *= 2

    return (new_dir)
