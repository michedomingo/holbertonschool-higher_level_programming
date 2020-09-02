#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL,
displays the body of the response
"""
import requests
from sys import argv


def printError1():
    req = requests.get(argv[1])
    if req.status_code < 400:
        print(req.text)
    else:
        print('Error code: {}'.format(req.status_code))


if __name__ == '__main__':
    printError1()
