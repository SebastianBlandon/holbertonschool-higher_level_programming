#!/usr/bin/python3
""" Module add integer
    Prototype: def add_integer(a, b=98):
    a and b must be integers or floats,
    otherwise raise a TypeError exception with the message a must be an integer
    or b must be an integer
    a and b must be first casted to integers if they are float
    Return the add of two numbers, a and b
"""


def add_integer(a, b=98):
    """ Funcion add_integer
        Args:
            a (int or float): input value
            b (int or float): input value
        Return:
            a + b or raise if it ocurred
    """
    if type(a) is int or type(a) is float:
        if type(b) is int or type(b) is float:
            return int(a) + int(b)
        else:
            raise TypeError("b must be an integer")
    else:
        raise TypeError("a must be an integer")
