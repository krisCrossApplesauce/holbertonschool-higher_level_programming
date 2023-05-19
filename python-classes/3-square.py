#!/usr/bin/python3
"""Write a class Square that defines a square (based on 2-square.py)"""


class Square:
    """square, now with area that returns the area of the square"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    
    def area(self):
        return (self.__size * self.__size)
