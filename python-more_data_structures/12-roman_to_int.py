#!/usr/bin/python3
def roman_to_int(roman_string):
    n = 0
    if roman_string is None:
        return n
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(len(roman_string)):
        if i + 1 != len(roman_string) and roman_dict[roman_string[i]] < roman_dict[roman_string[i + 1]]:
            n += roman_dict[roman_string[i + 1]] - roman_dict[roman_string[i]]
        elif i == 0 or roman_dict[roman_string[i]] <= roman_dict[roman_string[i - 1]]:
            n += roman_dict[roman_string[i]]
    return n
