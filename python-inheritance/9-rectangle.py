#!/usr/bin/python3
"""
a class Rectangle that inherits from BaseGeometry (7-base_geometry.py)
(based on 8-rectangle.py)
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle but now with area and print"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def print(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
