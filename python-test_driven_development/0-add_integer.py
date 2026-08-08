#!/usr/bin/python3
"""0-add_integer module.

Defines a function that adds two integers,
casting floats to integers first.
"""


def add_integer(a, b=98):
    """Add two integers or floats, casting floats to int first."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    try:
        a = int(a)
    except (OverflowError, ValueError):
        raise TypeError("a must be an integer")

    try:
        b = int(b)
    except (OverflowError, ValueError):
        raise TypeError("b must be an integer")

    return a + b
