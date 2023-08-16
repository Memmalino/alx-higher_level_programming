#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """program to print square of a matrix

    Args:
        matrix: the list of the square

    Returns:
        new matrix or None if null
    """
    if len(matrix) == 0 or matrix is None:
        return (None)
    new_matrix = []
    for i in matrix:
        new_matrix.append([x ** 2 for x in i])
    return (new_matrix)
