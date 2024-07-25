#!/bin/bash
# Send a GET request, check status code, and display the body if status code is 200
response=$(curl -s -w "%{http_code}" -o /tmp/body.txt "$1") && [ "${response: -3}" -eq 200 ] && cat /tmp/body.txt
