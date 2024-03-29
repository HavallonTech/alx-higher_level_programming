#!/usr/bin/python3

"""
a Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) == 1:
        data = ""
    else:
        data = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    payload = {"q": data}

    response = requests.post(url, data=payload)

    try:
        data = response.json()
        if data:
            print("[{}] {}".format(data['id'], data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
