#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    x = 0
    for i in a_dictionary:
        if i == key:
            x += 1
    if x != 0:
        del a_dictionary[key]
    return a_dictionary
