#!/usr/bin/python3
"""catch error"""


from sys import argv
from urllib.error import HTTPError
from urllib.request import urlopen

if __name__ == "__main__":
    url = argv[1]
    try:
        with urlopen(url, timeout=10) as response:
            res = response.read().decode("utf-8")
            print(response)
    except HTTPError as error:
        print("Error code: {}".format(error.status))
