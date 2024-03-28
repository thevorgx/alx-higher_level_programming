#!/usr/bin/python3
"""catch the http error"""


from sys import argv
from requests.exceptions import HTTPError
from requests import get

if __name__ == "__main__":
    url = argv[1]
    try:
        res = get(url)
        res.raise_for_status()
        print(res.text)
    except HTTPError as error:
        print("Error code: {}".format(error.response.status_code))
