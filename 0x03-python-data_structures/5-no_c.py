#!/usr/bin/python3
def no_c(my_string):
    ce = "cC"
    new_string = ''.join(x for x in my_string if x not in ce)
    return new_string
