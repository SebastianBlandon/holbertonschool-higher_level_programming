#!/usr/bin/python3
"""
    Function from_json_string(my_str)
"""
import json

def from_json_string(my_str):
    """ Function that returns an object (Python data structure)
    represented by a JSON string:

        Args:
            my_str (str): input str
    """
    return json.loads(my_str)
