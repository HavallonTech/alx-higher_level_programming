#!/usr/bin/python3


def replace_in_list(my_list, idx, myele):
    if (idx >= 0) and (idx < len(my_list)):
        my_list[idx] = myele
    return (my_list)
