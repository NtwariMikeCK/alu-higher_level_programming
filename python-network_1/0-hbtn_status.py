#!/usr/bin/python3
"""A script to fetch and display the content from a specific URL."""

import urllib.request  # Importing the urllib.request module to handle URL requests

def fetch_status():
    """Fetches the content of a URL and prints its type, content, and UTF-8 decoded content."""
    
    url = 'https://alu-intranet.hbtn.io/status'  # The URL to be fetched
    with urllib.request.urlopen(url) as response:
        # Opens the URL and retrieves the response
        body = response.read()
        # Reads the content of the response
        
    # Prints the details of the response body
    print("Body response:")
    print(f"    - type: {type(body)}")  # Prints the type of the response body
    print(f"    - content: {body}")  # Prints the raw content of the response body
    print(f"    - utf8 content: {body.decode('utf-8')}")  # Prints the UTF-8 decoded content of the response body

# If this script is executed directly, the fetch_status function is called
if __name__ == "__main__":
    fetch_status()
