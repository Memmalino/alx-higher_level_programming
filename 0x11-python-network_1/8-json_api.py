#!/usr/bin/python3
"""
This module Sends a post request to  a server with a letter as parameter
"""
import sys
import requests


if __name__ == "__main__":
    a = "" if len(sys.argv) == 1 else sys.argv[1]
    data = {"q": a}

    response = requests.post("http://0.0.0.0:5000/search_user", data)
    try:
        rsp = response.json()
        if rsp == {}:
            print("No result")
        else:
            print("[{}] {}".format(rsp.get("id"), rsp("name")))
    except ValueError:
        print("Not a valid JSON")
