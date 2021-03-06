#!/usr/bin/python3
"""
This module defines read_file
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, 'r') as f:
        read_data = f.read()
    print(read_data, end="")
