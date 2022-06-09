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
        if attrs:
            output = {}
            for i in attrs:
                for j in self.properties():
                    if j is i:
                        output[j] = self.__getattribute__(i)
            return output
        else:
            return self.__dict__

    def reload_from_json(self, json):
        self.first_name = json.get("first_name")
        self.last_name = json.get("last_name")
        self.age = json.get("age")
