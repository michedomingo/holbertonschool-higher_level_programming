#!/usr/bin/python3
"""
This is the "0-add_integer" module.

This module supplies one function - add_integer() - adds 2 integers.
"""


def add_integer(a, b=98):
    """
    Return sum of a and b which must be integers or floats.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')
    return int(a) + int(b)
