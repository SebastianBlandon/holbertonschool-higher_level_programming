#!/usr/bin/python3
"""
This is the "Square"  module.

This module provides a simple Square class.
"""


class Square:
    """ class Square create of size private attribute

    """
    def __init__(self, size=0, position=(0, 0)):
        """ Method __init__ initializes the class Square
            Args:
                size (int): sets the private attribute

            Return:
                Nothing
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ Method position property to retrieve position

        """
        return self.__position

    @position.setter
    def position(self, value):
        """ Method position to set self.__position with value

        Args:
            value (int): value to set the self.__position variable

        """
        if type(value) != tuple or len(value) != 2 or \
           not all([type(i) == int for i in value]) or \
           not all([i >= 0 for i in value]):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Method area calculates area given a size
            Args:
                Nothing

            Return:
                area calculates
        """
        return self.__size * self.__size

    def my_print(self):
        """ Method for print a square with character #

        """
        if not self.__size:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for i in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
