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

    def area(self):
        """
        Returns area of rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns rectangle description: [Rectangle] <width>/<height>
        """
        return "[Rectancle] " + str(self.__width) + "/" + str(self.__height)
