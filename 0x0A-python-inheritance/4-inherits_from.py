#!/usr/bin/python3
"""
    Function inherits_from(obj, a_class)
"""


def inherits_from(obj, a_class):
    """ Function that returns True if the object is an instance
    of a class that inherited (directly or indirectly) from the
    specified class ; otherwise False.

        Args:
            obj (object): input object
            a_class (class): input class

    """
    if obj.__class__ is not a_class:
        return (issubclass(obj.__class__, a_class))
    return False
