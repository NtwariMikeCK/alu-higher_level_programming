#!/usr/bin/python3
"""Fetches https://alu-intranet.hbtn.io/status using urllib."""

import urllib.request

def fetch_status():
    """Fetches the content of a URL and prints its type, content, and utf8 content."""
    url = 'https://alu-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        body = response.read()

    print("Body response:")
    print(f"    - type: {type(body)}")
    print(f"    - content: {body}")
    print(f"    - utf8 content: {body.decode('utf-8')}")

if __name__ == "__main__":
    fetch_status()
