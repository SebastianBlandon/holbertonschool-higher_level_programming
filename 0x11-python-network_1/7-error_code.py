#!/usr/bin/python3
"""
    Response header value #1
"""
import requests
from sys import argv

if __name__ == "__main__":
    URL = argv[1]
    response = requests.get(URL)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
