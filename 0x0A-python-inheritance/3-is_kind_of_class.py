#!/usr/bin/python3
"""
This module defines is_kind_of_class(obj, a_class)
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if object is an instance of,
    or if object is an instance of a class that inherited from,
    the specified class; otherwise False
    """
    return isinstance(obj, a_class)
