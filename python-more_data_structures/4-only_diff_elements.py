#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    in_one = []
    for i in set_1:
        x = 0
        for ii in set_2:
            if i != ii:
                x += 1
        if x == len(set_2):
            in_one.append(i)
    for a in set_2:
        x = 0
        for b in set_1:
            if a != b:
                x += 1
        if x == len(set_1):
            in_one.append(a)
    return in_one
