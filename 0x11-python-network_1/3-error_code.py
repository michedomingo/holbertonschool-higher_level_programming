#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL,
displays the body of the response
"""
import urllib.request
from sys import argv


def printError0():
    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == '__main__':
    printError0()
