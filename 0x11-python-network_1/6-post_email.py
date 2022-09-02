#!/usr/bin/python3
"""
    Response header value #1
"""
import requests
from sys import argv

if __name__ == "__main__":
    URL = argv[1]
    email = argv[2]
    data = {
        "email": email
    }
    response = requests.post(URL, data)
    print(response.text)
