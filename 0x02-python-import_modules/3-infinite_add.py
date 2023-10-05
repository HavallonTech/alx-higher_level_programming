#!/usr/bin/python3

if __name__ == "__main__":
    """A program that prints the  results of the addition of all arguments."""
    import sys

    total = 0

    for i in range(len(sys.argv) - 1):
        total += int(sys.argv[i + 1])
        print("{}".format(total))
