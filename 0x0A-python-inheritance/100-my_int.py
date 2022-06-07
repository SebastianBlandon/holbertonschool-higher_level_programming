#!/usr/bin/python3
"""
    This is the "MyInt"  module.

    This module provides a simple MyInt class.
"""


class MyInt(int):
    """ Empty class MyInt that defines a base geometry

        Args:
            int: inherits int attributes
    """
    def __init__(self, value):
        self.__value = value

    def __eq__(self, value):
        return False

    def __ne__(self, value):
        return True
