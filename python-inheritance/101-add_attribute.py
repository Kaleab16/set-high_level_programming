#!/usr/bin/python3
"""Module that defines a function to add attributes to objects if possible."""


def add_attribute(obj, name, value):
    """Add a new attribute to an object if it's possible."""
    if hasattr(obj, '__dict__') or hasattr(obj, '__slots__'):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
