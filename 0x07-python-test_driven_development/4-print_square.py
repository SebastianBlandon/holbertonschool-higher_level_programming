#!/usr/bin/python3
""" Module print square prints a square with the character #.
    Prototype: def print_square(size):
    size is the size length of the square
    size must be an integer, otherwise raise a
    TypeError exception with the message size must be an integer
    if size is less than 0, raise a ValueError
    exception with the message size must be >= 0
"""


def print_square(size):
    """ Funcion print_square
        Args:
            size (int): input value of size
        Return:
            Nothing
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    for i in range(size):
        print("#" * size)
