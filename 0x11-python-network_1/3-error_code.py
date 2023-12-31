#!/usr/bin/python3

"""
This is a module that displays error code or body response
"""

from urllib import request
from urllib.error import HTTPError
from sys import argv


if __name__ == '__main__':
    try:
        with request.urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print('Error code: {}'.format(e.code))
