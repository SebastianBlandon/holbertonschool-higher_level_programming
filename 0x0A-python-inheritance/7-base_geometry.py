#!/usr/bin/python3
"""
This is the "BaseGeometry"  module.

This module provides a simple BaseGeometry class.
"""


class BaseGeometry():
    """ Empty class BaseGeometry that defines a base geometry

        Args:
            Nothing

    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if (type(value) is not int):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
