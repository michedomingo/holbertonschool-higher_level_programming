#!/usr/bin/python3
"""
This module defines append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file
    after each line containing a specific string
    """
    with open(filename, 'r') as f:
        data = f.readlines()

    with open(filename, 'w') as f:
        string = ''
        for line in data:
            string += line
            if search_string in line:
                string += new_string
        f.write(string)
