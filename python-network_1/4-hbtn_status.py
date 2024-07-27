#!/usr/bin/python3
"""
This script sends a request to a given URL and displays the value of the
X-Request-Id variable found in the response headers.

Usage:
    ./5-hbtn_header.py <URL>

Requirements:
    - The first argument is the URL.
    - Only requests and sys modules are allowed.
"""

import requests

if __name__ == "__main__":
    url = 'https://alu-intranet.hbtn.io/status'
    response = requests.get(url)
    body = response.text

    print("Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")
