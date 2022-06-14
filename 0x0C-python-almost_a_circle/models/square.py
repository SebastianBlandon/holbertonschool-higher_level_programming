#!/usr/bin/python3
""" 3.Class Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square """

    def __init__(self, size, x=0, y=0, id=None):
        """ Class Constructor Method """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        i = self.id
        x = self.x
        y = self.y
        w = self.width
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(i, x, y, w)

    @property
    def size(self):
        """ size Getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size Setter """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args is not None and len(args) != 0:
            attrs = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for kw in kwargs:
                setattr(self, kw, kwargs[kw])

    def to_dictionary(self):
        """ Dictionary Method """
        to_dict = {'id': 0, 'size': 0, 'x': 0, 'y': 0}
        for key, value in to_dict.items():
            to_dict[key] = getattr(self, key)
        return to_dict
