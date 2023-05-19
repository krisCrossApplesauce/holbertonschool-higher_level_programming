#!/usr/bin/python3
"""Write a class Square that defines a square (based on 4-square.py)"""


class Square:
    """square but now with a method that prints the square"""
    def __init__(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            for ii in range(self.__size):
                print("#", end='')
            print("")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
