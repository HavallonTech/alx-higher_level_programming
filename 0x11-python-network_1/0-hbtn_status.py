#!/usr/bin/python3
"""
a python script to fetches https://alx-intranet.hbtn.io/status
"""


import urllib.request

target_url ='https://alx-intranet.hbtn.io/status'
with urllib.request.urlopen(target_url) as response:
    data = response.read()
    decoded_data = data.decode('utf-8')
    #print(decoded_data)
    #print(data)
    print(f"Body response:\n\t- type: {type(data)}")
    print(f"\t- content: {data}")
    #   print(f"\t- utf8 content: {the_page.decode('utf-8')}")
    print(f"\t- utf8 content: {decoded_data}")
