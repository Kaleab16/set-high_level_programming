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
    length = len(text)
    for i in range(length):
        char = text[i]
        if char == " " and line == "":
            continue
        line += char
        if char in ".?:":
            print(line.strip())
            if i != length - 1:
                print()
            line = ""
    if line.strip():
        print(line.strip(), end="")
