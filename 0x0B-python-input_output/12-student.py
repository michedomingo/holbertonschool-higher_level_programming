#!/usr/bin/python3
"""
This module define class Student
"""


class Student:
    """
    Defines a student by:
    Public instance attributes - first_name, last_name, age
    """
    def __init__(self, first_name, last_name, age):
        """Instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Public method retrieves dictionary representation of a Student instance
        """
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                new_dict[key] = value
        return new_dict
