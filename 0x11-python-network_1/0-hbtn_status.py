#!/usr/bin/python3
"""
    What's my status? #0
"""

if __name__ == "__main__":
    import urllib.request

    r = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(r) as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode("utf8")))
