#!/usr/bin/python3
""" the class Square that inherits from Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ a square """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def __str__(self):
        """ it returns info about the square """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
