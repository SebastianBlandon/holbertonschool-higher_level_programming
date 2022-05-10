#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    count = new_list.count
    index = new_list.index
    insert = new_list.insert
    pop = new_list.pop
    while (count(search) > 0):
        insert(index(search), replace)
        pop(index(search))
    return (new_list)
