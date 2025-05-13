#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers.

    Args:
        matrix : A list of lists of integers.
    """
    for row in matrix:
        for i, num in enumerate(row):
            if i > 0:
                print(" ", end="")
            print("{:d}".format(num), end="")
        print()

