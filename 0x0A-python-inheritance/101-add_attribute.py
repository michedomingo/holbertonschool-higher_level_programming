#!/usr/bin/python3
"""
This module is defines add_attribute()
"""


def add_attribute(object, attribute, value):
    """
    Adds a new attribute to an object if it’s possible
    """
    mc = getattr(object, "__doc__", None)
    if mc is None:
        setattr(object, attribute, value)
    else:
        raise TypeError("can't add new attribute")
