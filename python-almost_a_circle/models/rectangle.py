#!/usr/bin/python3
""" class Rectangle that inherits from Base """
from models.base import Base


class Rectangle(Base):
    """ a rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute """
        attributes = ["id", "width", "height", "x", "y"]
        if args is not None and len(args) > 0:
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
        elif kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def area(self):
        """ returns the area of the rectangle """
        return (self.__width * self.__height)

    def display(self):
        """ prints the rectangle using #'s to stdout """
        for iii in range(self.__y):
            print("")
        for i in range(self.__height):
            for iv in range(self.__x):
                print(" ", end='')
            for ii in range(self.__width):
                print("#", end='')
            print("")

    def __str__(self):
        """ returns info about the rectangle """
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__X

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
