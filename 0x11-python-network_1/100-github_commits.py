#!/usr/bin/python3
"""comment to update later"""


from sys import argv
from requests import get

if __name__ == "__main__":
    user = argv[1]
    repo = argv[2]
    url = f"https://api.github.com/repos/{user}/{repo}/commits"
    res = get(url)
    data = res.json()
    count = 1
    #data.reverse()
    for commit in data:
        if count <= 10:
            commit_data = commit.get('commit')
            commiter = commit_data.get('author').get('name')
            sha = commit.get('sha')
            print("{}: {}".format(sha, commiter))
            count += 1
        else:
            break
