#!/usr/bin/python3

import requests
import sys

def search_user():
    """ Send a POST request with a and process the response. """
    url = 'http://0.0.0.0:5000/search_user'
    
    # Get the letter from the command line argument, or set q="" if no argument is given
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    payload = {'q': q}
    
    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        try:
            json_response = response.json()
            if json_response:
                print(f"[{json_response.get('id')}] {json_response.get('name')}")
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
    except requests.RequestException as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    search_user()
