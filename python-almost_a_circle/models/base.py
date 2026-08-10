#!/usr/bin/python3
"""Base module.

Defines the Base class, which manages id attributes
for all future classes in this project.
"""
import json


class Base:
    """Base class that manages id and JSON (de)serialization."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dicts):
        """Return the JSON string representation of a list of dicts."""
        if list_dicts is None or len(list_dicts) == 0:
            return "[]"
        return json.dumps(list_dicts)

    @staticmethod
    def from_json_string(json_string):
        """Return a list represented by a JSON string."""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON representation of a list of objects to a file."""
        filename = "{}.json".format(cls.__name__)
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_dicts))

    @classmethod
    def create(cls, **dictionary):
        """Return an instance built from a dictionary of attributes."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances loaded from <ClassName>.json."""
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r", encoding="utf-8") as f:
                list_dicts = cls.from_json_string(f.read())
        except FileNotFoundError:
            return []
        return [cls.create(**d) for d in list_dicts]
