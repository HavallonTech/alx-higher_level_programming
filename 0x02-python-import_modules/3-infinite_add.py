#!/usr/bin/python3

if __name__ == "__main__":
    """A program that prints the  results of the 
    addition of all argumment"""

    from sys import argv
    count = len(argv)
    num = 0

    if count == 1:
        print(int(0))
    elif count > 1:
        for i in range(1, count):
            num = num + int(argv[i])

        print("{}".format(int(num)))

