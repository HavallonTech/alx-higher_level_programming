#!/usr/bin/python3
"""
rite a Python script that takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id in the response header
"""


import requests
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    http_req = requests.get(url)
    print(http_req.headers.get('X-Request-Id'))
