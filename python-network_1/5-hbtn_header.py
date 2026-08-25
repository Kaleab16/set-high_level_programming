#!/usr/bin/python3
"""Sends a request to URL and displays the X-Request-Id header value."""
import sys
import requests

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get("X-Request-Id"))
