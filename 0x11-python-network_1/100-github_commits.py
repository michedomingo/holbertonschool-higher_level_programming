#!/usr/bin/python3
"""
Lists 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
"""
import requests
from sys import argv


def listCommits():
    req = requests.get(
        'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1]))
    for commit in req.json()[0:10]:
        print('{}: {}'.format(commit.get('sha'), commit.get('commit')
                              .get('author').get('name')))


if __name__ == '__main__':
    listCommits()
