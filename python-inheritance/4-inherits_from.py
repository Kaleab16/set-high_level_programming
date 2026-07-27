#!/usr/bin/python3
"""Module that defines a function to check if an object inherited from a class."""


def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a class that inherited from a_class."""
    return type(obj) is not a_class and isinstance(obj, a_class)
