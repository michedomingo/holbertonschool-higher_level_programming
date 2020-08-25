#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL, displays the value of the
X-Request-Id variable found in the header of the response
"""
import urllib.request
from sys import argv


def printHeader0():
    with urllib.request.urlopen(argv[1]) as response:
        print(response.getheader('X-Request-Id'))


if __name__ == '__main__':
    printHeader0()
