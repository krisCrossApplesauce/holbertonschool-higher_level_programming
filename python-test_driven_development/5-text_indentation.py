#!/usr/bin/python3
"""a function that prints a text with 2 new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """prints text but indented"""
    x = 0
    if type(text) is not str:
        raise TypeError("text must be a string")
    else:
        for i in text:
            if x == 0:
                print("{}".format(i), end='')
                if i == '.' or i == '?' or i == ':':
                    print("\n")
                    x = 1
            else:
                x = 0
