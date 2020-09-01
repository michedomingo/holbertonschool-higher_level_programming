#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status
"""
import requests


def printStatus1():
    body = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(body.text)))
    print("\t- content: {}".format(body.text))

if __name__ == '__main__':
    printStatus1()
