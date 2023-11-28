#!/usr/bin/python3

"""A funtion to add two number"""


def add_integer(a, b=98):
    """
       Args:
       a: as an integer
       b: as an integer

       Return: It returns the addition of a and b
     """

    if (not isinstance(a, (int, float))):
        raise TypeError("a must be an integer")
    if (not isinstance(b, (int, float))):
        raise TypeError("b must be an integer")
    result = int(a) + int(b)
    return (result)


if __name__ == "__main__":

    t = add_integer(67, 89)
    print(t)
