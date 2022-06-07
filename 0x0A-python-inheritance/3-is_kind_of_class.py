#!/usr/bin/python3
"""
    Function is_kind_of_class(obj, a_class)
"""


def is_kind_of_class(obj, a_class):
    """ Function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False.

        Args:
            obj (object): input object
            a_class (class): input class
    """
    return isinstance(obj, a_class)
