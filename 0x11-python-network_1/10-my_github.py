#!/usr/bin/python3
"""
Takes your Github credentials (username and password)
Uses the Github API to display your id
"""
import requests
from sys import argv


def myGithub():
    req = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    print(req.json().get('id'))


if __name__ == '__main__':
    myGithub()
