#!/usr/bin/python3
"""
A module contains a function that divides each element of a matriX
"""


def matrix_divided(matrix, div):
    """"
    function that divides all elements of a matrix.

    Args:
        matrix: list of list of ints or/and floats
        div: the element that divides the matrix

    Raises:
        TypeError:
            must be list of lists
            all elements must be an int or float
    Returns:
        the divided matrix
    """
    new_matrix = []
    if (type(div) is not int) and (type(div) is not float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) is not list:
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )
    if len(matrix) == 0:
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )
    for i in matrix:
        row_len = len(matrix[0])
        if type(i) is not list:
            raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
                    )
        if len(i) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for j in i:
            if (type(j) is not int) and (type(j) is not float):
                raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )
            res = j / div
            new_ele = float("{:.2f}".format(res))
            new_row.append(new_ele)

        new_matrix.append(new_row)
    return (new_matrix)
