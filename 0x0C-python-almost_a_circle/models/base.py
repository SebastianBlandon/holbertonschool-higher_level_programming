#!/usr/bin/python3
""" 1.Class Base """
import json
import turtle as t


class Base():
    """ Class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Class Constructor Method """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ To JSON string Method """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save To File Method """
        filename = cls.__name__ + ".json"
        list_out = []
        if list_objs is not None:
            for obj in list_objs:
                _dict_ = obj.to_dictionary()
                list_out.append(_dict_)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_out))

    @staticmethod
    def from_json_string(json_string):
        """ From JSON String Static Method"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Create Method """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Load From File Method """
        filename = cls.__name__ + ".json"
        list_out = []
        try:
            with open(filename, "r") as f:
                list_obj = cls.from_json_string(f.read())
                for _dict_ in list_obj:
                    list_out.append(cls.create(**_dict_))
                return list_out
        except Exception:
            return list_out

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Save To File Method """
        if list_objs is None:
            return []
        filename = cls.__name__ + ".csv"
        list_out = []
        for obj in list_objs:
            _dict_ = obj.to_dictionary()
            list_out.append(_dict_)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_out))

    @classmethod
    def load_from_file_csv(cls):
        """ Load From File Method """
        filename = cls.__name__ + ".csv"
        list_out = []
        try:
            with open(filename, "r") as f:
                list_obj = cls.from_json_string(f.read())
                for _dict_ in list_obj:
                    list_out.append(cls.create(**_dict_))
                return list_out
        except Exception:
            return list_out

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ Draw Method """
        colors = ["purple", "red", "blue", "green", "yellow", "white"]
        index = 0
        t.bgcolor("gray")
        for obj in list_rectangles:
            t.color(colors[index])
            t.up()
            t.fd(obj.x)
            t.rt(90)
            t.fd(obj.y)
            t.lt(90)
            t.pendown()
            t.fd(obj.width)
            t.rt(90)
            t.fd(obj.height)
            t.rt(90)
            t.fd(obj.width)
            t.rt(90)
            t.fd(obj.height)
            t.up()
            t.home()
            index += 1
        for obj in list_squares:
            t.color(colors[index])
            t.up()
            t.fd(obj.x)
            t.rt(90)
            t.fd(obj.y)
            t.lt(90)
            t.pendown()
            t.fd(obj.width)
            t.rt(90)
            t.fd(obj.height)
            t.rt(90)
            t.fd(obj.width)
            t.rt(90)
            t.fd(obj.height)
            t.up()
            t.home()
            index += 1
        t.color("black")
        t.done()
