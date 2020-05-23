#!/usr/bin/python3
"""
This is the "2-matrix_divided" module.

This module supplies one function - matrix_divided()
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix - list of lists of integers or floats
    """
    list_error = 'matrix must be a matrix (list of lists) of integers/floats'

    if type(matrix) is not list:
        raise TypeError(list_error)

    for row in matrix:
        if type(row) is not list:
            raise TypeError(list_error)
        for elements in row:
            if not isinstance(elements, (int, float)):
                raise TypeError(list_error)
        if len(row) is not len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    new_matrix = []
    for row in matrix:
        if not isinstance(div, (int, float)):
            raise TypeError('div must be a number')
        else:
            new_matrix.append([round((elements / div), 2) for elements in row])

    return new_matrix
