#!/usr/bin/python3
"""
This module deflines pascal_triangle
"""


def pascal_training(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n
    """
    new_list = []
    if n <= 0:
        return new_list
    for i in range(n):
        row = [1]
    """WIP"""
