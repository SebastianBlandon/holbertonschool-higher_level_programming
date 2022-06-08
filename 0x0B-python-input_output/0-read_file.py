#!/usr/bin/python3
"""
    Function read_file(filename="")
"""


def read_file(filename=""):
    """ Function function that reads a text file (UTF8) and prints it to stdout:

        Args:
            file (file with str): input file
    """
    f = open(filename, 'r', encoding="utf-8")
    print(f.read(), end='')
    f.close()
