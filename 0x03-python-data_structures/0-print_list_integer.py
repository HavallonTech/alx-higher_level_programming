#!/usr/bin/python3
# a function that prints all integers in a list
# 0-print_list_integer.py


def print_list_integer(my_list=[]):
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
