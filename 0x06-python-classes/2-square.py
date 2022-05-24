#!/usr/bin/python3
"""
This is the "Square"  module.

This module provides a simple Square class.
"""


class Square:
    """ class Square create of size private attribute

    """
    def __init__(self, size=0):
        """ Method __init__ initializes the class Square
            Args:
                size (int): sets the private attribute

        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
