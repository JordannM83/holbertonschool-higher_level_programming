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
    # Vérification de div
    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Vérification que matrix est une liste non vide
    if not isinstance(matrix, list) or not matrix:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    # Vérification que tous les éléments sont des listes
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")

    # Vérification que toutes les lignes ont la même taille
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

    # Vérification que tous les éléments sont des nombres
    for row in matrix:
        for element in row:
            if (not isinstance(element, (int, float)) or
                    isinstance(element, bool)):
                raise TypeError("matrix must be a matrix (list of lists) of "
                                "integers/floats")

    # Création de la nouvelle matrice
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)

    return new_matrix
