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

    def to_json(self):
        """
        Public method retrieves dictionary representation of a Student instance
        """
        return self.__dict__
