#!/usr/bin/python3
"""
a function that prints a text with 2 new lines after each of these characters:
.
?
:
"""


def text_indentation(text):
    """prints text but indented"""
    x = 0
    if type(text) is not str:
        raise TypeError("text must be a string")
    else:
        for i in text:
            if x == 0 or i != ' ':
                if x == 1:
                    x = 0
                print("{}".format(i), end='')
                if i == '.' or i == '?' or i == ':':
                    print("\n")
                    x = 1
