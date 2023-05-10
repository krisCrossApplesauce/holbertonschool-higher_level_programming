#!/usr/bin/python3
import string
for i in range(0, 26):
    if i != 4 and i != 16:
        print("{}".format(string.ascii_lowercase[i]), end="")
