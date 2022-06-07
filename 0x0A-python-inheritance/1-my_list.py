#!/usr/bin/python3
"""
This is the "MyList"  module.

This module provides a simple MyList class.
"""


class MyList(list):
    """ Empty class MyList that defines a list

        Args:
            list: inherits from list

    """
    def print_sorted(self):
        print(sorted(self))
