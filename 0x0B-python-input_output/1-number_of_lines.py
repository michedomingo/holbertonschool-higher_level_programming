#!/usr/bin/python3
"""
This module defines number_of_lines
"""


def number_of_lines(filename=""):
    """
    Returns the number of lines of a text file
    """
    count = 0
    with open(filename, 'r') as f:
        for line in f:
            count += 1
    return count
