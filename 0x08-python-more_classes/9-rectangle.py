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
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Method __init__ initializes the class Rectangle
            Args:
                width (int): sets the private attribute
                height (int): sets the private attribute

        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """ Method __str__ print the rectangle with the character #

        """
        to_print = ""
        if not self.__height or not self.width:
            return to_print
        for i in range(self.__height):
            for j in range(self.__width):
                try:
                    to_print += str(self.print_symbol)
                except Exception:
                    to_print += type(self).print_symbol
            if i is not self.__height - 1:
                to_print += "\n"
        return to_print

    def __repr__(self):
        """ Method __repr__ return a string representation of the rectangle
            to be able to recreate a new instance by using eval()

        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """ Method __del__ Print the message Bye rectangle...
            (... being 3 dots not ellipsis)
            when an instance of Rectangle is deleted

        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """ Method width property to retrieve width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Method width property setter to set width
            Args:
                value (int): width to setter
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
                value (int): height to setter
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Method area calculates area given a width and height
            Args:
                Nothing
            Return:
                area calculates
        """
        return self.__width * self.__height

    def perimeter(self):
        """ Method perimeter calculates perimeter given a width and height
            Args:
                Nothing
            Return:
                perimeter calculates
        """
        if not self.__width or not self.__height:
            return 0
        return 2 * self.__width + 2 * self.__height

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
