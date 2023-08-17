#!/usr/bin/python3

def square_matrix_simple(matrix):
    """Create a new matrix of the same size as the inputx matrix"""
    result = [[0 for i in range(len(matrix[0]))] for i in range(len(matrix))]

    """iterate through each elemnt of the matrix and compute its square"""
    for element in range(len(matrix)):
        for j in range(len(matrix[i])):
            result[i][j] = matrix[i][j] ** 2

    return result
