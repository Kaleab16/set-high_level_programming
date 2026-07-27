#!/usr/bin/python3
"""Module that defines a function to look up an object's attributes/methods."""


def lookup(obj):
    """Returns a list of available attributes and methods of an object."""
    return dir(obj)
