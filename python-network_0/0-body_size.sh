#!/bin/bash
# Sends a request to the given URL and displays the size of the
# response body, in bytes, using curl.
curl -s -o /dev/null -w "%{size_download}\n" "$1"
