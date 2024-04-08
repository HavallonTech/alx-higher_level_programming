#!/usr/bin/python3
"""Finds the peak in a list of unsorted list of integers"""


def find_peak(list_of_integers):
    """Finds a peak in list_of_integers"""
    if list_of_integers is None or list_of_integers == []:
        return None
    the_low = 0
    the_hi = len(list_of_integers)
    mid = ((the_hi - the_low) // 2) + the_low
    mid = int(mid)
    if the_hi == 1:
        return list_of_integers[0]
    if the_hi == 2:
        return max(list_of_integers)
    if list_of_integers[mid] >= list_of_integers[mid - 1] and list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
