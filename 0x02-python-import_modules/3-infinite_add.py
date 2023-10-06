#!/usr/bin/python3

if __name__ == "__main__":
    #A program that prints the  results of the addition of all arguments.

    import sys, math
    result = 0
    for i in sys.argv:
        result += int(i)
        print("{}".format(result))

