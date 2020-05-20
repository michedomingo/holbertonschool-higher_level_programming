#!/usr/bin/python3
class Square:
    """
    This is a class Square that defines a square
    by a private instance attribute: size
    - property def size(self): to retrieve size
    - property setter def size(self, value): to set size
    - size must be an integer and >= 0
    - raise error exceptions on invalid inputs
    - public instance method: def area(self): returns square area size
    - square instance can answer to comparators:
        ==, !=, >, >=, < and <= (compares square area between Square objects)
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

    def __eq__(self, other):
        """
        square area of first object and other object are equal
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        square area of first object and other object are not equal
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        square area of first object is greater than other
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        square area of first object is greater than or equal to other
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        square area of first object is smaller than other
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        square area of first object is smaller than or equal to other
        """
        return self.area() <= other.area()
