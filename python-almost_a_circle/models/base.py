#!/usr/bin/python3
""" a class called Base """
import json


class Base:
    """ Base class of all other classes in this project """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return "{}".format(json.dumps(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """
        if list_objs is not None:
            list_objs = [obj.to_dictionary() for obj in list_objs]
        else:
            list_objs = []
        with open(cls.__name__ + ".json", "w") as file:
            file.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            dummy = cls(0, 0)
        elif cls.__name__ == "Square":
            dummy = cls(0)
        dummy.update(**dictionary)
        return dummy
