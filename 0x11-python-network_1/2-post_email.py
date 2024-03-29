#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays the body of
the response (decoided in utf-8)
"""


from urllib.request import urlopen, Request
from urllib import parse
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    email = {'email': argv[2]}
    data = parse.urlencode(email).encode('ascii')
    req = Request(url, data)

    with urlopen(req) as response:
        result = response.read()
        header = result.decode('utf-8')
        print(header)
