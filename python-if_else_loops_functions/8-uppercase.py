#!/usr/bin/python3
import string
def uppercase(str):
    x = 0
    for i in str:
        val = ord(str[x])
        if val >= 97 and val <= 122:
            print("{}".format(string.ascii_uppercase[val - 97]), end="")
        else:
            print("{}".format(str[x]), end="")
        x = x + 1
