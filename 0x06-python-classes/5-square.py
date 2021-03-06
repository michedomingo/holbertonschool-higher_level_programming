#!/usr/bin/python3
"""This module creates a class Square"""


class Square:
    """
    This is a class Square that defines a square
    by a private instance attribute: size
    - property def size(self): to retrieve size
    - property setter def size(self, value): to set size
    - size must be an integer and >= 0
    - raise error exceptions on invalid inputs
    - public instance method: def area(self): returns square area size
    - public instance method: def my_print(self): prints square w/ # to stdout
    """

    def __init__(self, size=0):
        """
        Initializes class Square by size
        """
        self.size = size

    @property
    def size(self):
        """
        to retrieve size - defines size of class Square, returns value of size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        to set value - defines value of class Square size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        returns current square area
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints square with # to stdout
        """
        if self.__size is 0:
            print()
        for i in range(self.__size):
            print("#" * self.__size)
