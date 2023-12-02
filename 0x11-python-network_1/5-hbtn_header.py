#!/usr/bin/python3
"""
This module is used to get response header X-Request-Id
"""
import requests
from sys import argv


if __name__ == '__main__':
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
