#!/usr/bin/python3
"""
This module is for class BaseGeometry
"""


class BaseGeometry:
    """
    Public instance methods:
    *def area(self), def integer_validator(self, name, value)
    """
    def area(self):
        """
        Raises an Exception with the message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value input type is correct
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise TypeError(name + " must be greater than 0")
