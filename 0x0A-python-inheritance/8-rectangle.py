#!/usr/bin/python3
"""
This module is for class BaseGeometry/Rectancle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class Rectangle inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Private instantiation of width and height attributes
        validated by integer_validator
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
