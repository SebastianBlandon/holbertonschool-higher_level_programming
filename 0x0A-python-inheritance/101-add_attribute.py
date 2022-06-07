#!/usr/bin/python3
"""
    Function add_attribute(class, name_attr, new_attr)
"""


def add_attribute(new_obj, name_attr, new_attr):
    """ Function that adds a new attribute to an object if it’s possible:

        Args:
            new_obj (object): input class
            name_attr (str): input str
            new_attr (anyone): input anyone type

    """
    if getattr(new_obj, "__doc__", None) is None:
        setattr(new_obj, name_attr, new_attr)
    else:
        raise TypeError("can't add new attribute")
