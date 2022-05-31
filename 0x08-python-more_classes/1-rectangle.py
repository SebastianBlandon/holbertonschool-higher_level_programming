#!/usr/bin/python3
"""
This is the "Rectangle"  module.

This module provides a simple Rectangle class.
"""


class Rectangle():
    """ Empty class Rectangle that defines a rectangle

        Args:
            Nothing

    """
    def __init__(self, width=0, height=0):
        """ Method __init__ initializes the class Rectangle
            Args:
                size (int): sets the private attribute

        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ Method width property to retrieve width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Method width property setter to set width
            Args:
                width (int): width to setter
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Method size property to retrieve size
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ Method height property setter to set height
            Args:
                height (int): height to setter
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
