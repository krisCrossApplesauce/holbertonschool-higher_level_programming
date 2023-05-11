#!/usr/bin/python3
def uppercase(str):
    for char in str:
        val = ord(char)
        if val >= 97 and val <= 122:
            char = chr(val - 32)
        print("{}".format(char), end='')
    else:
        print()
