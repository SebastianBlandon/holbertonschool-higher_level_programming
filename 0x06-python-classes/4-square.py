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

            Return:
                Nothing
        """
        self.size = size

    @property
    def size(self):
        """ Method size property to retrieve size

        """
        return self.__size

    @size.setter
    def size(self, size):
        """ Method sizeproperty setter to set size

            Args:
                size (int): size to setter
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Method area calculates area given a size
            Args:
                Nothing

            Return:
                area calculates
        """
        return self.__size * self.__size
