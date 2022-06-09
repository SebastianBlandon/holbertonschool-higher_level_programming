#!/usr/bin/python3
"""
    Function to_json_string(my_obj)
"""
import json


def to_json_string(my_obj):
    """ Function that returns the JSON representation of an object (string):
        Args:
            my_obj (class): input class
    """
    return json.dumps(my_obj)
