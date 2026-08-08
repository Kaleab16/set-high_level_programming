#!/usr/bin/python3
"""Module for converting an object to its JSON string representation."""
import json


def to_json_string(my_obj):
    """Return the JSON string representation of an object."""
    return json.dumps(my_obj)
