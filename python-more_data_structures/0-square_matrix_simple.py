#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append([])
        for ii in matrix[i]:
            new_matrix[i].append(ii * ii)
    return new_matrix
