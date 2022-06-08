#!/usr/bin/python3
"""
    Function append_write(filename="", text="")
"""


def append_write(filename="", text=""):
    """ Function function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added:

        Args:
            filename (str): input str
            text (str): input str
    """
    with open(filename, 'a', encoding="utf-8") as f:
        size_write = f.write(text)
    return size_write
