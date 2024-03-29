#!/usr/bin/python3
"""python script that use git api, if username and password(token) is correct
print the id, if not print None.

for future vorg:
1-you used the respond status_code to check if authentification
is a success, parsed to a json format so you can use get to get the id.

2-mistakes you did, you tried to use data instead of headers for a get request
remember, data is for POST(request.post)
and headers for a REQUEST(request.get)."""

from sys import argv
from requests import get

if __name__ == "__main__":
    username = argv[1]
    url = "https://api.github.com/users/{}".format(username)
    password = argv[2]
    password_dict = {'Authorization': f"token {password}"}
    res = get(url, headers=password_dict)

    if res.status_code == 200:
        data = res.json()
        user_id = data.get("id")
        print(user_id)
    else:
        print("None")
