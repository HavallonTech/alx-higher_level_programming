#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = none
    finally:
        print("Inside result: {}".format(result))
        #print("Inside result:",formatted_value)
        return (result)
