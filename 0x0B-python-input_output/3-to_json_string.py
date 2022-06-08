#!/usr/bin/python3
import json
"""
    Function to_json_string(my_obj)
"""


def to_json_string(my_obj):
    """ Function that returns the JSON representation of an object (string):

        Args:
            filename (str): input str
            text (str): input str
    """
    return json.dumps(my_obj)
