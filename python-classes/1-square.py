#!/usr/bin/python3
"""Write a class Square that defines a square (based on 0-square.py)"""


class Square:
    """the new and improved square! now with the size attribute"""
    __size = None

    def __init__(self, new_size=None):
        self.__size = new_size
