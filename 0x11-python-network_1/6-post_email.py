#!/usr/bin/python3
"""
Takes in a URL and an email address, sends a POST request to the passed URL
with the email as a parameter, and finally displays the body of the response
"""
import requests
from sys import argv


def printEmail1():
    data = {'email': argv[2]}
    req = requests.post(argv[1], data)
    print(req.text)


if __name__ == '__main__':
    printEmail1()
