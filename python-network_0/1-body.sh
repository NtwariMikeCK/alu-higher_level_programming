#!/bin/bash
# Send a GET request to the URL and get both headers and body
response=$(curl -s -w "%{http_code}" -o /tmp/body.txt "$1")

# Check if the status code is 200
if [ "$response" -eq 200 ]; then
    # Display the body of the response
    cat /tmp/body.txt
fi
