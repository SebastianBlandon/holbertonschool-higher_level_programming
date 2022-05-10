#!/usr/bin/python3
def weight_average(my_list=[]):
    nume = 0
    deno = 0
    if not len(my_list):
        return 0
    for tupl in my_list:
        nume += (tupl[0] * tupl[1])
        deno += tupl[1]
    return nume / deno
