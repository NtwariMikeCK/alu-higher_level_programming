#!/usr/bin/python3
"""
A script to fetch and display the content from a specific URL.
"""

import urllib.request

def fetch_status():
    """Fetches content from a URL and prints its details."""
    url = 'https://alu-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        body = response.read()
        
    print("Body response:")
    print(f"    - type: {type(body)}")
    print(f"    - content: {body}")
    print(f"    - utf8 content: {body.decode('utf-8')}")

if __name__ == "__main__":
    fetch_status()
