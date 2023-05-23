#!/usr/bin/python3
"""a function that divides each number in a matrix by a number"""


def matrix_divided(matrix, div):
    """yup"""
    div_matrix = []
    if type(div) != float and type(div) != int:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in range(len(matrix)):
        if i + 1 != len(matrix) and len(matrix[i]) != len(matrix[i + 1]):
            raise TypeError("Each row of the matrix must have the same size")
        div_matrix.append([])
        for ii in matrix[i]:
            if type(ii) != float and type(ii) != int:
                raise TypeError("matrix must be a matrix " +
                                "(list of lists) of integers/floats")
            div_matrix[i].append(round(ii / div, 2))
    return div_matrix
