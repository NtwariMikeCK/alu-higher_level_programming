#!/bin/bash
# Send an OPTIONS request to the URL and display the allowed methods from the Allow header
curl -s -I "$1" | grep -i "Allow:" | sed 's/Allow: //i'
