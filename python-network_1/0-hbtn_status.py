#!/usr/bin/python3
# python script that fetches 'https://alu-intranet.hbtn.io/status'
"""
    fetch 'https://intranet.hbtn.io/status'
"""
import urllib.request

url = "https://alu-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    content = response.read()
    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", expected_content)
    print("\t- utf8 content:", expected_content.decode("utf-8"))

