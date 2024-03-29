#!/usr/bin/python3
"""comment to update later"""


from sys import argv
from requests import get

if __name__ == "__main__":
    user = argv[1]
    repo = argv[2]
    url = f"https://api.github.com/repos/{user}/{repo}/commits?per_page=10"
    res = get(url)
    if res.status_code == 200:
        data = res.json()
        for commit in data:
            commit_data = commit.get('commit')
            commiter = commit_data.get('author').get('name')
            sha = commit.get('sha')
            print("{}: {}".format(sha, commiter))
