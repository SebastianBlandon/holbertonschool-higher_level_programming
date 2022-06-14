#!/usr/bin/python3
""" 2.Class Rectangle """
from models.base import Base


class Rectangle(Base):
    """ Class Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Class Constructor Method """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        i = self.id
        x = self.__x
        y = self.__y
        w = self.__width
        h = self.__height
        return "[Rectangle] ({}) {}/{} - {}/{}".format(i, x, y, w, h)

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
            raise ValueError("width must be > 0")
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
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Method x property to retrieve x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """ Method x property setter to set x
            Args:
                value (int): x to setter
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Method y property to retrieve y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """ Method y property setter to set y
            Args:
                value (int): y to setter
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Method area calculates area given a width and height
            Args:
                Nothing
            Return:
                area calculates
        """
        return self.__width * self.__height

    def display(self):
        """ Display Method """
        print("\n" * self.__y, end="")
        for row in range(self.__height):
            if self.__x != 0:
                print(" " * self.__x, end="")
            print("#" * self.__width)

    def update(self, *args, **kwargs):
        """ Update Method with key-worded argument """
        if args is not None and len(args) != 0:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for kw in kwargs:
                setattr(self, kw, kwargs[kw])

    def to_dictionary(self):
        """ Dictionary Method """
        to_dict = {'id': 0, 'width': 0, 'height': 0, 'x': 0, 'y': 0}
        for key, value in to_dict.items():
            to_dict[key] = getattr(self, key)
        return to_dict
