#!/usr/bin/python3
class Square:
    """
    This is a class Square that defines a square
    by a private instance attribute: size
    - size must be an integer and >= 0
    - raise error exceptions on invalid inputs
    - public instance method: def area(self): returns square area size
    """

    def __init__(self, size=0):
        """
        Initializes class Square by size
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        returns current square area
        """
        return self.__size ** 2
