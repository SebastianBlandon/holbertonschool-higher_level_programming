#!/usr/bin/python3
def max_integer(my_list=[]):
    if (not len(my_list)):
        return None
    max_int = -1000
    for i in range(len(my_list)):
        if (max_int < my_list[i]):
            max_int = my_list[i]
    return max_int
