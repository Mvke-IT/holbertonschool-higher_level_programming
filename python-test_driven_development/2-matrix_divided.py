#!/usr/bin/python3
"""
This module contains a function that divide a mtrix
named matrix_divided that you pass 2 arguments
the matrix and the number to divide for
"""


def matrix_divided(matrix, div):
    """
    This function divide a matrix by the
    number number passed to us

    matrix = matrix to be divided
    div = number to be divided from
    """
    msg_error = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(msg_error)

    if type(div) not in [int, float]:
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    for row in matrix:
        for value in row:
            if type(value) not in [int, float]:
                raise TypeError(msg_error)

    first_row = len(matrix[0])
    for row in matrix:
        if first_row != len(row):
            raise TypeError('Each row of the matrix must have the same size')

<<<<<<< HEAD
    return [[round(i / div, 2) for i in row] for row in matrix]
=======
    return [[round(i / div, 2) for i in row] for row in matrix]
>>>>>>> 1ffe2787dd3992ad30fa28f39cb9c087feeb5b30
