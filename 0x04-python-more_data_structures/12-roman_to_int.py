#!/usr/bin/python3
def roman_to_int(roman_string):
    int_string = []
    int_value = 0
    flag = 0
    if ((type(roman_string) != str) or (roman_string is None)):
        return int_value
    for i in range(len(roman_string)):
        if roman_string[i] == "I":
            int_string.append(1)
        elif roman_string[i] == "V":
            int_string.append(5)
        elif roman_string[i] == "X":
            int_string.append(10)
        elif roman_string[i] == "L":
            int_string.append(50)
        elif roman_string[i] == "C":
            int_string.append(100)
        elif roman_string[i] == "D":
            int_string.append(500)
        elif roman_string[i] == "M":
            int_string.append(1000)
        else:
            return int_value
    for i in range(len(int_string)):
        if (i < len(int_string) - 1 and int_string[i] < int_string[i + 1]):
            int_value = int_string[i + 1] - int_string[i]
            flag = 1
        elif flag:
            flag = 0
        else:
            int_value += int_string[i]
    return int_value
