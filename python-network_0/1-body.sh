#!/bin/bash
# Send a GET request and display the body if the status code is 200
curl -s -w "%{http_code}" -o /tmp/body.txt "$1" | grep -q '200' && cat /tmp/body.txt
