#!/usr/bin/python3
"""
Module for reading text files.
"""

def read_file(filename=""):
    """
    Reads a text file(UTF8) and prints it to stdout.

    args:
         filename(str): The name of the file to read. Defaults to"".
    """
    with open(filename,encoding="utf-8") as f:
        print(f.read(),end="")
