#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        if (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            division = a / b
    except ZeroDivisionError:
        division = None
    finally:
        print("Inside result: {}".format(division))
        """print("Inside result:",formatted_value)"""
        return (division)
