#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    intcount = 0
    for a in range(0, x):
        try:
            if type(my_list[a]) is int:
                print("{:d}".format(my_list[a]), end="")
                incount = incount + 1
        except:
            pass
    print("")
    return (intcount)
