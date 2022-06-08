#!/usr/bin/python3
"""
    Function write_file(filename="", text="")
"""


def write_file(filename="", text=""):
    """ Function function that writes a string to a text file (UTF8)
    and returns the number of characters written:

        Args:
            filename (str): input str
            text (str): input str
    """
    with open(filename, 'w', encoding="utf-8") as f:
        size_write = f.write(text)
    return size_write
