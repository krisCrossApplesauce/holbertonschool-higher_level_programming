#!/usr/bin/python3
"""Write a class Square that defines a square (based on 1-square.py)"""


class Square:
    """Square but making sure size is an int and is < 0"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
