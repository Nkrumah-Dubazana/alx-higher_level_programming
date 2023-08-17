#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """computes the square value of all integers of a matrix."""
    square_matrix = list(map(lambda row: list(map(lambda num: ** 2, row)), matrix))
    return squared_matrix
