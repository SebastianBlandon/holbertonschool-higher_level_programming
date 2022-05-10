#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    for keys in new_dict.keys():
        i = new_dict.get(keys)
        i = i * 2
        new_dict[keys] = i
    return new_dict
