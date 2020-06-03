#!/usr/bin/python3
"""
This module is for class MyInt
"""


class MyInt(int):
    """
    Inherits from int
    """
    def __eq__(self, other):
        """
        Equal operator inverted
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Not equal operator inverted
        """
        return super().__eq__(other)
