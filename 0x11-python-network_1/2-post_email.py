#!/usr/bin/python3
"""
    POST an email #0
"""
from sys import argv

if __name__ == "__main__":
    import urllib.request
    from urllib.parse import urlencode

    email = {"email": argv[2]}
    encoded_data = urlencode(email).encode("utf-8")
    req = urllib.request.Request(argv[1], encoded_data)
    with urllib.request.urlopen(req) as response:
        page = response.read()
        print(page.decode("utf-8"))
