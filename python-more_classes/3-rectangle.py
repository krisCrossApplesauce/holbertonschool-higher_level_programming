#!/usr/bin/python3
"""Write a class Rectangle that defines a rectangle (based on 2-rectangle)"""


class Rectangle:
    """rectangle but now with print() and str()"""
    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            p = 0
        else:
            p = (self.__width * 2) + (self.__height * 2)
        return p

    def __str__(self):
        str = ""
        if self.__width != 0 and self.__width != 0:
            for i in range(self.__height):
                for ii in range(self.__width):
                    str += "#"
                if i + 1 != self.__height:
                    str += "\n"
        return str

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
