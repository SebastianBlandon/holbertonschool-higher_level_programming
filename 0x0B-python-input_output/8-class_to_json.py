#!/usr/bin/python3
"""
    Function class_to_json(obj)
"""


def class_to_json(obj):
    """ Function that returns the dictionary description
    with simple data structure (list, dictionary, string,
    integer and boolean) for JSON serialization of an object:

        Args:
            obj (class): input class
    """
    return obj.__dict__
