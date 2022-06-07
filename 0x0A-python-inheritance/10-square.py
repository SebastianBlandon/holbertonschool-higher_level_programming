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

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        return (self.__width * self.__height)

"""
This is the "Square"  module.

This module provides a simple Square class.
"""


class Square(Rectangle):
    """ Empty class Square that defines a square of a rectangle

        Args:
            Nothing

    """
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)

    def area(self):
        return pow(self.__size, 2)
