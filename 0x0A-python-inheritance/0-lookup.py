#!/usr/bin/python3
"""
This module defines a function that defines lookup function
to return the list of an object attribute
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object
    """
    return dir(obj)
