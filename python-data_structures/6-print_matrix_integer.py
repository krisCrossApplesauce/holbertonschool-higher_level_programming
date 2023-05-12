#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 0:
        print("")
    for i in matrix:
        if len(i) == 0:
            print("")
        for ii in range(len(i)):
            print("{:d}".format(i[ii]), end=" " if ii + 1 < len(i) else "\n")
