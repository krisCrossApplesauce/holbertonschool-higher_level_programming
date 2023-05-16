#!/usr/bin/python3
def best_score(a_dictionary):
    best = None
    if a_dictionary is None or len(a_dictionary) == 0:
        return best
    for i in a_dictionary:
        if best is None:
            best = i
        if a_dictionary[i] > a_dictionary[best]:
            best = i
    return best
