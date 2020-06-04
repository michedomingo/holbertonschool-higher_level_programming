#!/usr/bin/python3
"""
This module defines write_file
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8)
    Returns the number of characters written
    """
    with open(filename, 'w') as f:
        num_of_chars = f.write(text)
    return num_of_chars
