#!/usr/bin/python3
import math
"""
This is the "MagicClass"  module.

This module provides a simple MagicClass class.
"""


class MagicClass:
    """ class MagicClass create of

    """
    def __init__(self, radius=0):
        """ Method __init__ initializes the class MagicClass
            Args:
                radius (int): sets the private attribute

            Return:
                Nothing
        """
        if type(radius) != int or type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """ Method area calculates area of circumference given a radius
            Args:
                Nothing

            Return:
                area calculates
        """
        return pow(self.__radius, 2) * math.pi

    def circumference(self):
        """ Method for to calculate circumference of circle

        """
        return 2 * math.pi * self.__radius
