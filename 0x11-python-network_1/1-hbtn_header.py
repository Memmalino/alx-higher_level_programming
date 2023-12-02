#!/usr/bin/python3

"""
this modeule is used to get response header-
X-Request-Id
"""

import urllib.request
import sys

if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.info().get('X-Request-Id'))
