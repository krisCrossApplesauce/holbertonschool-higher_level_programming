#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    n = 0
    for i in range(len(roman_string)):
        if i + 1 != len(roman_string) and roman_dict[roman_string[i]] < roman_dict[roman_string[i + 1]]:
            n += roman_dict[roman_string[i + 1]] - roman_dict[roman_string[i]]
            i += 1
        else:
            n += roman_dict[roman_string[i]]
    return n
