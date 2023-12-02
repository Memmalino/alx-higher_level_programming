#!/usr/bin/python3

"""
This module is used to post email to a port 500
"""

from urllib import parse, request
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    pst = parse.urlencode({'email': argv[2]}).encode('utf-8')
    with request.urlopen(url, pst) as response:
        print(response.read().decode('utf-8'))


