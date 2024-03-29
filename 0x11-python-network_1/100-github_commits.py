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

    for commit in data:
        if count <= 10:
            commit_data = commit.get('commit')
            commiter = commit_data.get('committer').get('name')
            sha = commit_data.get('tree').get('sha')
            print("{}: {}".format(sha, commiter))
            count += 1
        else:
            break
