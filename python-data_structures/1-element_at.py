#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or my_list[idx] == None:
        return None
    else:
        return my_list[idx]
