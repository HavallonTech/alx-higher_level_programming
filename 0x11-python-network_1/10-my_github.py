#!/usr/bin/python3

"""
 Python script that takes your GitHub credentials (username
and password) and uses the GitHub API to display your id
"""

import requests
from sys import argv
from requests.auth import HTTPBasicAuth


if __name__ == '__main__':
    url = 'https://api.github.com/user'
    user = argv[1]
    password = argv[2]
    data = HTTPBasicAuth(user, password)

    req = requests.get(url, auth=data)

    user = req.json()

    print(user.get('id'))
