#!/usr/bin/python3
"""This module creates a class Rectangle"""


class Rectangle:
    """
    This is an emty class Rectangle that defines a rectangle
    *private instance attributes: width and height
    *public instance methods: area, perimeter, str, repr
    """
    def __init__(self, width=0, height=0):
        """Initializes class Rectangle by width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieve width - defines and returns width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """set/define value of width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """retrieve height - defines and return height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """set/define value of height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """return rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """return rectangle perimeter"""
        if self.__width is 0 or self.__height is 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """return rectangle as # string"""
        string = ""
        if self.__height == 0 or self.__width == 0:
            return string
        for row in range(self.__height):
            string += ('#' * self.__width)
            if row is not self.__height - 1:
                string += '\n'
        return string

    def __repr__(self):
        """return string representation to recreate new instance"""
        return 'Rectangle({}, {})'.format(self.__width, self.__height)
