#!/usr/bin/python3
"""Response header value"""


from urllib.request import urlopen, Request
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    value = "X-Request-Id"
    req = Request(url)
    with urlopen(req) as res:
        print(res.headers.get(value))
