#!/usr/bin/python3
"""
This is the "5-text_indentation" module.

This module supplies one function - text_identation()
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after characters . ? :
    """
    if type(text) is not str:
        raise TypeError('text must be a string')
    new_line = text.replace('.', '.\n\n')
    new_line = new_line.replace('?', '?\n\n')
    new_line = new_line.replace(':', ':\n\n')
    split_strings = new_line.split('\n')
    for string in range(len(split_strings)):
        print('{}'.format(split_strings[string].strip()),
              end=('' if (string == (len(split_strings) - 1)) else '\n'))
