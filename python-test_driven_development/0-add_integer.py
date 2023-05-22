#!/usr/bin/python3
"""a function that adds two integers"""


def add_integer(a, b=98):
    """this function is actually for understanding how to make tests"""
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    if type(a) == int and type(b) == int:
        return a + b
    else:
        if type(a) != int:
            raise TypeError("a must be an integer")
        if type(b) != int:
            raise TypeError("b must be an integer")
