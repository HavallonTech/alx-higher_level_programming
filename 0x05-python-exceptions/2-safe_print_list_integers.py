#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    intcount = 0
    lent = 0

    for list_len in my_list:
        lent = lent + 1

    try:
        for b in range(0, x):
            if isinstance(my_list[b], (int)):
                print("{}".format(my_list[b], end=""))
                intcount = intcount + 1
    except IndexError:
        print("list index out of range")
    except:
        print("other error")
    finally:
        print("")
        return(intcount)
