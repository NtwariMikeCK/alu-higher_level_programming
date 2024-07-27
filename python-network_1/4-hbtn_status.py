#!/usr/bin/python3
#Fetches https://alu-intranet.hbtn.io/st

import requests

def fetch_status():
    """Fetches the content of a URL and """
    url = 'https://alu-intranet.hbtn.io/status'
    response = requests.get(url)
    body = response.text

    print("Body response:")
    print(f"    - type: {type(body)}")
    print(f"    - content: {body}")

if __name__ == "__main__":
    fetch_status()
