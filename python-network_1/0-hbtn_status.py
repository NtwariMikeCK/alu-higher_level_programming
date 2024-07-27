#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL, and displays the.
the X-Request-Id variable found in the header of the response.
"""
import urllib.request
#imports the requests.
def fetch_status():
#Fetches the content of a URL and prints its type, cont.
    url = 'https://alu-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        body = response.read()
#opens the url.
    print("Body response:")
    print(f"    - type: {type(body)}")
    print(f"    - content: {body}")
    print(f"    - utf8 content: {body.decode('utf-8')}")
#the print .
if __name__ == "__main__":
    fetch_status()
