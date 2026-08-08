#!/usr/bin/python3
"""Module for converting a class instance's attributes to a dictionary."""


def class_to_json(obj):
    """Return the dictionary description of a simple-attribute object."""
    return obj.__dict__
