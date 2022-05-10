#!/usr/bin/python3
def best_score(a_dictionary):
    best_score = -1000
    find_one = 0
    key = ""
    if a_dictionary is None:
        return None
    for keys in a_dictionary.keys():
        i = a_dictionary.get(keys)
        if best_score < i:
            best_score = i
            key = keys
            find_one = 1
    if find_one:
        return key
    return None
