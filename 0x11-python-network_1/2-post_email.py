#!/usr/bin/python3

"""post an email value to the url, and request it
https://blog.finxter.com/how-to-send-a-post-request
-using-urllib-in-python/
"""

from sys import argv
from urllib.parse import urlencode
from urllib.request import Request, urlopen

if __name__ == "__main__":
    url = argv[1]
    email_value = argv[2]
    data = {'email': email_value}
    req = Request(url, urlencode(data))
    with urlopen(req) as response:
        res = response.read()
        print(res.decode('utf-8'))
