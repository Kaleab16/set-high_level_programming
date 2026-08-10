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
