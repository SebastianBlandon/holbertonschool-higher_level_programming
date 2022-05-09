#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = list(tuple_a) + [0]*2
    tuple_b = list(tuple_b) + [0]*2
    new_tuple = [sum(x) for x in zip(tuple_a, tuple_b)]
    return tuple(new_tuple[0:2])
