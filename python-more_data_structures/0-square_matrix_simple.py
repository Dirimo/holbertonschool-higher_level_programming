#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a matrix.

    Args:
        matrix: A 2 dimensional array.

    Returns:
        A new matrix with the same size as matrix, where each value
        is the square of the corresponding value in the input matrix.
        The initial matrix is not modified.
    """
    new_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
            new_row.append(num ** 2)
        new_matrix.append(new_row)
    return new_matrix
