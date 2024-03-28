#!/usr/bin/python3
"""Response header value using requests"""


from sys import argv
from requests import get

if __name__ == "__main__":
    url = argv[1]
    value = "X-Request-Id"
    res = get(url, data=value)
    print(res.headers.get(value))
