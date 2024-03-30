#!/usr/bin/python3


"""
Time for an interview!
takes 2 arguments in order to solve this challenge.
"""
import requests
from sys import argv


if __name__ == '__main__':
    my_repo = argv[1]
    name = argv[2]
    url = f'https://api.github.com/repos/{name}/{my_repo}/commits'

    req = requests.get(url)
    result = req.json()

    for commit in result[:10]:
        sha = commit.get('sha')
        author_name = commit.get('commit').get('author').get('name')
        print(f"{sha}: {author_name}")
