#!/usr/bin/python3
"""
rite a Python script that takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id in the response header
"""


import requests
from sys import argv

if __name__ == '__main__':
    if len(argv) < 2:
        print("Please provide a URL as a command line argument.")
        exit(1)

    url = argv[1]
    req = requests.get(url)

    if req.status_code == 200:
        x_request_id = req.headers.get('X-Request-Id')
        if x_request_id:
            print(f'X-Request-Id: {x_request_id}')
        else:
            print("X-Request-Id header not found in the response.")
    else:
        print(f"HTTP Error: {req.status_code}")
