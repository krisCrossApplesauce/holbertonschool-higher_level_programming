#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    a = 0
    while i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            a += 1
        except IndexError:
            break
        except ValueError:
            pass
        except TypeError:
            pass
        i += 1
