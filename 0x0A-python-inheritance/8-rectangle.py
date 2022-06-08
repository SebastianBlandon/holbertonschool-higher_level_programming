#!/usr/bin/python3


BaseGeometry = __import__("7-base_geometry").BaseGeometry
"""
This is the "Rectangle"  module.

This module provides a simple Rectangle class.
"""


class Rectangle(BaseGeometry):
    """ Empty class Rectangle that defines a rectangle
        inherits from BaseGeometry

        Args:
            Nothing

    """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
