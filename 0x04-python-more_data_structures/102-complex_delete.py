#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    save_keys = []
    for keys in a_dictionary.keys():
        val = a_dictionary.get(keys)
        if value == val:
            save_keys.append(keys)
    for i in range(len(save_keys)):
        del a_dictionary[save_keys[i]]
    return a_dictionary
