#!/usr/bin/python3
"""
This module defines is_same_class(obj, a_class)
"""


def is_same_class(obj, a_class):
    """
    Returns True if object is exactly an instance of specified class,
    otherwise False
    """
    return type(obj) == a_class
