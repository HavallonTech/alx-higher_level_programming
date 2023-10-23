#!/usr/bin/python3

def safe_print_integer(value):

    check = 0
    if isinstance(value, (int)):
        formatted_value = "{:d}".format(value)
        check = 1
    else:
        formatted_value = "{}".format(value)
        check = 2
    try:
        print(formatted_value)
        if (check == 1):
            return (True)
        else:
            return (False)
    except (TypeError, ValueError):
        print("type error")
