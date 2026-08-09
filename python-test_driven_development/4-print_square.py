#!/usr/bin/python3
"""4-print_square module.

Defines a function that prints a square of '#' characters.
"""


def print_square(size):
    """Print a square of size `size` using the '#' character."""
    if isinstance(size, bool) or not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")

    if isinstance(size, float):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
