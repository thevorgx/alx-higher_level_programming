#!/usr/bin/python3
"""What's my status"""


import requests

if __name__ == "__main__":
    req = requests.get("https://alx-intranet.hbtn.io/status")
    content = req.text
    print("Body response:")
    print("{}- type: {}".format("\t", type(content)))
    print("{}- content: {}".format("\t", content))
