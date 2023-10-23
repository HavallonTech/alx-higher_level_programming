#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    try:
        for b in range(0, x):
            print(f"{my_list[b]}", end="")
        return (x)
    except IndexError:
        b = 0
        for a in my_list:
            b = b + 1
            x = b
    finally:
        print("")
    return (x)
