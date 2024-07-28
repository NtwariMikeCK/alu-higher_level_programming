#!/usr/bin/python3
"""Fetches GitHub user ID using  a personal access token."""

import requests
import sys


def fetch_github_id(username, token):
    """Fetches and prints the personal access token."""
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, token))
    if response.status_code == 200:
        user_data = response.json()
        print(user_data.get("id"))
    else:
        print(None)

if __name__ == "__main__":
    # Get username and token from command-line arguments
    username = sys.argv[1]
    token = sys.argv[2]
    fetch_github_id(username, token)
