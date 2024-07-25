#!/bin/bash
# Send a GET request and display the body if status code is 200
response=$(curl -s -w "%{http_code}" -o /tmp/body.txt "$1") && [ "$response" -eq 200 ] && cat /tmp/body.txt
