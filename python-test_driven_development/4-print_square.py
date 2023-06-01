#!/usr/bin/python3
"""a function that prints a square with the character #"""


def print_square(size):
    """it prints a square"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            for ii in range(size):
                print("#", end='')
            print("")
