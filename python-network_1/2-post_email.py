#!/usr/bin/python3
"""Sends a request to a URL and handles HTTPError by printing status code."""
import sys
import urllib.error
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print(body.decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
