#!/usr/bin/python3
"""
    Function lookup(obj)
"""


def lookup(obj):
    """ Function that returns the list of available
        attributes and methods of an object:

        Args:
            obj (object): input object

    """
    return dir(obj)
