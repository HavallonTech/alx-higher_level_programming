#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the
URL and displays the body of the response (decoded in utf-8).
"""


import requests

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes

        print(f'Body response:\n\t- type: {type(response.text)}')
        print(f'\t- content: {response.text}')
    except requests.exceptions.RequestException as e:
        print(f'Error occurred: {e}')
