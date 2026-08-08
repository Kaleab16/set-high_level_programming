#!/usr/bin/python3
"""Module for inserting text after lines matching a search string."""


def append_after(filename="", search_string="", new_string=""):
    """Insert new_string after each line containing search_string."""
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
