#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    intcount = 0

    try:
        for b in range(0, x):
            if isinstance(my_list[b], (int)):
                print("{:d}".format(my_list[b], end=""))
                intcount = intcount + 1
            else:
                continue
        print("")
        return (intcount)
    except (IndexError):
        print("list index out of range")
    except:
        print("other error")
