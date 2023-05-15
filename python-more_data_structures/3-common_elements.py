#!/usr/bin/python3
def common_elements(set_1, set_2):
    in_both = []
    for i in set_1:
        for ii in set_2:
            if i == ii:
                in_both.append(i)
    return in_both
