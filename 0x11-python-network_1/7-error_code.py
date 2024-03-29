#!/usr/bin/python3

"""
Write a Python script that takes in a URL, sends a request to the URL
and displays the body of the response.
"""
import requests
from sys import argv


url = sys.argv[1]

  req = requests.get(url)
   if req.status_code >= 400:
        print("Error code:", req.status_code)
    else:
        print(req.text)
