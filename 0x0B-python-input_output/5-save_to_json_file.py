#!/usr/bin/python3
import json
"""
    Function save_to_json_file(my_obj, filename)
"""


def save_to_json_file(my_obj, filename):
    """ Function that writes an Object to a text file,
    using a JSON representation:

        Args:
            my_obj (class): input class
            filename (str): input str
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
