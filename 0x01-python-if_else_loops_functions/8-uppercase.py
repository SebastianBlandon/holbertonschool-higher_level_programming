#!/usr/bin/python3
def uppercase(str):
    str = list(str)
    for i in range(len(str)):
        if (ord(str[i]) >= 97 and ord(str[i]) <= 122):
            str[i] = chr(ord(str[i]) - 32)
        print(str[i], end="")
    print()
