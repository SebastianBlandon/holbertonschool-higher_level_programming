#!/usr/bin/python3
def remove_char_at(str, n):
    if (n <= -1 or n > len(str)):
        return (str)
    str = str[:n] + str[n + 1 - len(str):]
    return (str)
