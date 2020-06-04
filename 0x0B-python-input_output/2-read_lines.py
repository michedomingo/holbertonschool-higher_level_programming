#!/usr/bin/python3
"""
This module defines read_lines
"""


def read_lines(filename="", nb_lines=0):
    """
    Reads n lines of a text file (UTF8) and prints it to stdout
    """
    count = len(open(filename).readlines())
    with open(filename, 'r') as f:
        if nb_lines > 0 and nb_lines < count:
            while nb_lines:
                print(f.readline(), end="")
                nb_lines -= 1
        else:
            read_data = f.read()
            print(read_data, end="")
