#!/usr/bin/python3
"""
This module is for class Rectangle/Square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class Square inherits from Rectangle
    """
    def __init__(self, size):
        """
        Private instantiation of size attribute
        validated by integer_validator
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Returns area of square
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns the square description: [Square] <width>/<height>
        """
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
