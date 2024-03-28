#!/usr/bin/python3
"""catch error"""


from sys import argv
from urllib.error import HTTPError
from urllib.request import urlopen, Request

if __name__ == "__main__":
    url = argv[1]
    req = Request(url)
    try:
        with urlopen(req) as response:
            res = response.read().decode("utf-8")
            print(res)
    except HTTPError as error:
        print("Error code: {}".format(error.status))
