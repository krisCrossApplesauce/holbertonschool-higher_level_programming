#!/usr/bin/python3
""" the class Square that inherits from Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ a square """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ it returns info about the square """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)