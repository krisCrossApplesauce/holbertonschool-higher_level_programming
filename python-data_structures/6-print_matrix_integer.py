#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for ii in range(len(i)):
            print("{:d}".format(i[ii]), end=" " if ii + 1 < len(i) else "\n")
