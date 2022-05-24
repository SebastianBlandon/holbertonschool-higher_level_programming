#!/usr/bin/python3
"""
This is the "Square"  module.

This module provides a simple Square class.
"""


class Square:
    """ class Square create of size private attribute

    """
    def __init__(self, size):
        """ Method __init__ initializes the class Square
            Args:
                size (int): sets the private attribute

        """
        self.__size = size
