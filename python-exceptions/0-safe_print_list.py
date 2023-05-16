#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    a = 0
    i = 0
    while i in range(x):
        try:
            print("{}".format(my_list[i]), end='')
            a += 1
        except IndexError:
            break
        i += 1
    print("")
    return a
