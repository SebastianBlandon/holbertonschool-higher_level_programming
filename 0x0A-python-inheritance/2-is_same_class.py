#!/usr/bin/python3
"""
    Function is_same_class(obj, a_class)
"""


def is_same_class(obj, a_class):
    """ Function that returns True if the object is exactly an instance
        of the specified class ; otherwise False.

        Args:
            obj (object): input object
            a_class (class): input class
    """
    return (obj.__class__ is a_class)
