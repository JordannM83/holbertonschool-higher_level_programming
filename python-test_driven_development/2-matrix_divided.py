#!/usr/bin/python3
"""
Module that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.

    Args:
        matrix: list of lists of integers or floats
        div: number to divide by

    Returns:
        A new matrix with all elements divided by div

    Raises:
        TypeError: if matrix is not a list of lists of integers/floats
        TypeError: if each row of the matrix doesn't have the same size
        TypeError: if div is not a number
        ZeroDivisionError: if div is equal to 0
    """
    new_matrix = []
    i = 0
    for matrice in matrix:
        new_matrix.append([])
        for num in matrice:
            new_matrix[i].append(round(num / div, 2))
        i += 1
    return new_matrix
