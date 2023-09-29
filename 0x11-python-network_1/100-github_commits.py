#!/usr/bin/python3
"""Python script that lists 10 commits of a repo
"""
from requests import get, auth
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    r = get(url)
    r_json = r.json()
    for i in range(10):
        key = r_json[i]
        print("{}: {}".format(key.get('sha'), key.get('commit')
                              .get('author').get('name')))
