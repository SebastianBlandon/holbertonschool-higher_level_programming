#!/usr/bin/python3
"""
    Metohd Class Student
"""


class Student():
    """
        class Student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def properties(self):
        return [i for i in self.__dict__.keys() if i[:1] != '_']

    def to_json(self, attrs=None):
        if not type(attrs) is list:
            return self.__dict__
        if not all(type(item) is str for item in attrs):
            return self.__dict__
        if attrs:
            output = {}
            for i in attrs:
                for j in self.properties():
                    if j is i:
                        output[j] = self.__getattribute__(i)
            return output
        else:
            return self.__dict__
