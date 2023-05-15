#!/usr/bin/python3
def uniq_add(my_list=[]):
    a = 0
    for i in range(len(my_list)):
        x = 0
        for ii in range(0, i):
            if my_list[i] == my_list[ii]:
                x += 1
        if x == 0:
            a += my_list[i]
    return a
