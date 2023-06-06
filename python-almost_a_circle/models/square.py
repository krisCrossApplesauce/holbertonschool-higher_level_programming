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

    def update(self, *args, **kwargs):
        """ assigns an assignment to each attribute """
        attributes = ["id", "size", "x", "y"]
        if args is not None and len(args) > 0:
            for attr, value in zip(attributes, args):
                if attr == "size":
                    self.width = value
                    self.height = value
                else:
                    setattr(self, attr, value)
        elif kwargs is not None:
            for key, value in kwargs.items():
                if key == "size":
                    self.width = value
                    self.height = value
                else:
                    setattr(self, key, value)

    def __str__(self):
        """ it returns info about the square """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
