#!/usr/bin/python3

"""
Write a Python script that takes in a URL, sends a request to the URL
and displays the body of the response.
"""
import requests
from sys import argv


if __name__ == '__main__':
    http_req = requests.get(argv[1])

    if http_req.status_code >= 400:
        print(f'Error code: {req.status_code}')
    else:
        print(http_req.text)
