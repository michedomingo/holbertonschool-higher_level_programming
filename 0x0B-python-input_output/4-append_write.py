#!/usr/bin/python3
"""
This module defines append_write
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8)
    Returns the number of characters added
    """
    with open(filename, 'a') as f:
        num_of_chars = f.write(text)
    return num_of_chars
