#!/usr/bin/python3
def write_file(filename="", text=""):
    """Write text to a file (UTF8) and return the number of characters written."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
