#!/usr/bin/python3
"""
a python script to fetches https://alx-intranet.hbtn.io/status
"""


import urllib.request

target_url ='https://alx-intranet.hbtn.io/status'
with urllib.request.urlopen(target_url) as response:
    data = response.read()
    #print(decoded_data)
    #print(data)
    print(f"Body response:\n\t- type: {type(data)}")
    print(f"\t- content: {data}")
    print(f"\t- utf8 content: {data.decode('utf-8')}")
