#!/usr/bin/python3
"""
This module defines class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    This class Rectangle inherits from Base
    Defines private instance attributes with public getter/setter
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize class Rectangle instance
        Call the super class Base id and logic via __init__
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def validate_argument(self, arg, value):
        """Validate input"""
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(arg))
        if value <= 0 and (arg is 'width' or arg is 'height'):
            raise ValueError('{} must be > 0'.format(arg))
        if value < 0 and (arg is 'x' or arg is 'y'):
            raise ValueError('{} must be >= 0'.format(arg))

    @property
    def width(self):
        """Get width property"""
        return self.__width

    @width.setter
    def width(self, width):
        """Set the width"""
        self.validate_argument('width', width)
        self.__width = width

    @property
    def height(self):
        """Get height property"""
        return self.__height

    @height.setter
    def height(self, height):
        """Set the height"""
        self.validate_argument('height', height)
        self.__height = height

    @property
    def x(self):
        """Get property x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Set x"""
        self.validate_argument('x', x)
        self.__x = x

    @property
    def y(self):
        """Get property y"""
        return self.__y

    @y.setter
    def y(self, y):
        """Set y"""
        self.validate_argument('y', y)
        self.__y = y

    def area(self):
        """Returns the area value of the Rectangle instance"""
        return self.__width * self.__height
