#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""
import requests
from sys import argv


def apiSearch():
    if len(argv) == 1:
        q = ''
    else:
        q = argv[1]

    req = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        data = req.json()
        if data:
            print('[{}] {}'.format(data.get('id'), data.get('name')))
        else:
            print('No result')
    except:
        print('Not a valid JSON')


if __name__ == '__main__':
    apiSearch()
