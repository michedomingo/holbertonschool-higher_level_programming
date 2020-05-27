#!/usr/bin/python3
"""This module creates a class Rectangle"""


class Rectangle:
    """
    This class Rectangle defines a rectangle
    *private class attribute: number_of_instances counts instances
    *public class attribute: print_symbol use # for string representation
    *private instance attributes: width and height
    *public instance methods: area, perimeter, str, repr, del
    *static method: bigger_or_equal returns largest rectangle based on area
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes class Rectangle by width and height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        for height in range(self.__height):
            for width in range(self.__width):
                string += str(self.print_symbol)
            string += '\n'
        return string[:-1]

    def __repr__(self):
        """return string representation to recreate new instance"""
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        """print message when Rectangle instance is deleted"""
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns largest rectangle based on area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
