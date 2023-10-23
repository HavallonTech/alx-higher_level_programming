#!/usr/bin/python

def safe_print_list(my_list=[], x=0):

    count = 0

    for b in range(x):
        try:
            print("{}".format(my_list[b]), end="")
            count = count + 1
        except IndexError:
            print("Index Error")
        finally:
            print("")
    return (count)
