#!/usr/bin/python3
"""
This module is used to  make http request, print error code on error
"""
import requests
from sys import argv


if __name__ == '__main__':
    response = requests.get(argv[1])
    try:
        response.raise_for_status()
        print(response.content.decode(response.encoding))
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(e.response.status_code))
