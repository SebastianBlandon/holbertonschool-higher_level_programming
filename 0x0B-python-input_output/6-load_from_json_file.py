#!/usr/bin/python3
import json
"""
    Function load_from_json_file(filename)
"""


def load_from_json_file(filename):
    """ Function that creates an Object from a “JSON file”:

        Args:
            filename (str): input str
    """
    with open(filename, 'r', encoding="utf-8") as f:
        output = json.loads(f.read())
    return output
