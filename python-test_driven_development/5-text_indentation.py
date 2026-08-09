#!/usr/bin/python3
"""5-text_indentation module.

Defines a function that prints text with extra newlines
after each '.', '?', and ':'.
"""


def text_indentation(text):
    """Print text with 2 new lines after '.', '?', and ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = ""
    for char in text:
        if char == " " and line == "":
            continue
        line += char
        if char in ".?:":
            print(line.strip())
            print()
            line = ""
    if line.strip():
        print(line.strip(), end="")
