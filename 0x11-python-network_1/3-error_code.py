#!/usr/bin/python3
"""
     Error code #0
"""
from sys import argv

if __name__ == "__main__":
    import urllib.request
   
    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read()
            print(html.decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.status))
