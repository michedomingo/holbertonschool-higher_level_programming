#!/usr/bin/python3
"""
This module defines class Base
"""


class Base:
    """
    Defines the “base” of all other classes in this project
    to manage id attribute/avoid code duplicating
    *private class attribute: __nb_objects
    *public instance attribute: id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize class Base instance by id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
