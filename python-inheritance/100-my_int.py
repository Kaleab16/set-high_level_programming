#!/usr/bin/python3
"""Module that defines a rebel MyInt class."""


class MyInt(int):
    """MyInt class that inherits from int with inverted == and != operators."""

    def __eq__(self, other):
        """Override == operator to be inverted."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override != operator to be inverted."""
        return super().__eq__(other)
