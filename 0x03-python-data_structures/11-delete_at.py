#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if (not len(my_list)):
        return None
    if (-1 < idx < len(my_list)):
        del my_list[idx]
    return my_list
