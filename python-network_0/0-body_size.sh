#!/usr/bin/bash

# Check if exactly one argument is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 URL"
    exit 1
fi

# URL to fetch
url=$1

# Fetch the URL using curl and display the size of the response body in bytes
curl -s "$url" | wc -c
