#!/usr/bin/python3
# 4-new_in_list.py


def new_in_list(my_list, indx, ele):
    """Replace an element in a copied list at a specific position."""
    if (indx < 0) or (indx > (len(my_list) - 1)):
        return (my_list)

    copy = [x for x in my_list]
    copy[indx] = ele
    return (copy)
