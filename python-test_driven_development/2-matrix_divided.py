#!/usr/bin/python3
"""
This is the "2-matrix_divided" module.
"""


def matrix_divided(matrix, div):
    """
    All elements of the matrix should
    be divided by div, rounded to 2 decimal places
    """
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(msg)

    for row in matrix:
        if type(row) is not list:
            raise TypeError(msg)
        for item in row:
            if type(item) not in [int, float]:
                raise TypeError(msg)

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []
    for row in matrix:
        new_row = []
        for item in row:
            new_row.append(round(item / div, 2))
        new_matrix.append(new_row)

    return new_matrix
