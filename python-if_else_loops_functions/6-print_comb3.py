#!/usr/bin/python3
for i in range(10):
    for ii in range(10):
        if ii > i:
            print("{}{}".format(i, ii), end=", " if i != 8 else '\n')
