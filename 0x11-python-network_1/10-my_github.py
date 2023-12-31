#!/usr/bin/python3
"""
This module is used to query github api for user id
"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv


if __name__ == '__main__':
    response = requests.get(
        'https://api.github.com/users/' + argv[1],
        auth=HTTPBasicAuth(argv[1], argv[2])
    )
    print(response.json().get('id'))
