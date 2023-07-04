#!/usr/bin/python3
"""This module is called 2-matrix_divided.
    It contains a function that divides all elaments
    of a matrix
"""


def matrix_divided(matrix, div):
    """The function matrix_divided divides all elements of a matrix

    Args:
        matrix (list): The matrix to be divided
        div (int or float): The number used to divide each element
        of the matrix

    Raises:
        TypeError: is raised if the matrix is not a list of lists of
        integers or float
        TypeError: raised if any row is not of the same size
        TypeError: raised if div is not a number
        ZeroDivisionError: raised if div is zero

    Returns:
        list: The new matrix with each element divided by div
        and rounded of to 2 d.p.
    """
    if not matrix or not isinstance(matrix, list):
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats')
    for row in matrix:
        if not row or not isinstance(row, list):
            raise TypeError(
                'matrix must be a matrix (list of lists) of integers/floats')
        length = len(matrix[0])
        if length != 0 and len(row) != length:
            raise TypeError('Each row of the matrix must have the same size')
        for digit in row:
            if not isinstance(digit, (int, float)):
                raise TypeError(
                    'matrix must be a matrix (list of lists) of ' +
                    'integers/floats')
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    new = [[round(element / div, 2) for element in row] for row in matrix]
    return new
