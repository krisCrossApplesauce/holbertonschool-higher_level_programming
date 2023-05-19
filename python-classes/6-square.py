#!/usr/bin/python3
"""Write a class Square that defines a square (based on 5-square.py)"""


class Square:
    """square but now with position"""
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if type(position) is not tuple or len(position) != 2 \
            or type(position[0]) is not int or type(position[1]) is not int \
                or position[0] < 0 or position[1] < 0:
                raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size != 0:
            for v in range(self.__position[1]):
                print("")
        else:
            for iv in range(self.__position[0]):
                print(" ", end='')
            print("")
        for i in range(self.__size):
            for iii in range(self.__position[0]):
                print(" ", end='')
            for ii in range(self.__size):
                print("#", end='')
            print("")

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2 \
            or type(value[0]) is not int or type(value[1]) is not int \
                or value[0] < 0 or value[1] < 0:
                raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
