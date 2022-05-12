#!/usr/bin/python3
def roman_to_int(roman_string):
    int_string = []
    int_value = 0
    flag = 0
    if ((type(roman_string) != str) or (roman_string is None)):
        return int_value
    convert = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(len(roman_string)):
        if roman_string[i] in convert:
            int_string.append(convert[roman_string[i]])
        else:
            return int_value
    for i in range(len(int_string)):
        if (i < len(int_string) - 1 and int_string[i] < int_string[i + 1]):
            int_value += int_string[i + 1] - int_string[i]
            flag = 1
        elif flag:
            flag = 0
        else:
            int_value += int_string[i]
    return int_value
