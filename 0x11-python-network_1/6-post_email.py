#!/usr/bin/python3
"""post an email, and get it back"""


from sys import argv
from requests import post

if __name__ == "__main__":
    url = argv[1]
    email_value = argv[2]
    data = {'email': email_value}
    req = post(url, data=data)
    print(req.text)
