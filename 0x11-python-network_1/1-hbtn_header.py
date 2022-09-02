#!/usr/bin/python3
"""
    Response header value #0
"""
from sys import argv

if __name__ == "__main__":
    import urllib.request

    r = urllib.request.Request(argv[1])
    with urllib.request.urlopen(r) as response:
        hs = response.headers.items()
        for h in hs:
            if h[0] == "X-Request-Id":
                print(h[1])
