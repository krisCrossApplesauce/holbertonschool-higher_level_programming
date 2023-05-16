#!/usr/bin/python3
def roman_to_int(roman_string):
    n = 0
    if isinstance(roman_string, str) == False:
        return n
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(len(roman_string)):
        if i + 1 != len(roman_string) and \
                d[roman_string[i]] < d[roman_string[i + 1]]:
            n += d[roman_string[i + 1]] - d[roman_string[i]]
        elif i == 0 or d[roman_string[i]] <= d[roman_string[i - 1]]:
            n += d[roman_string[i]]
    return n
