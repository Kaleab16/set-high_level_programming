#!/usr/bin/python3
"""Fetches intranet.htbn.io/status and displays the body using requests."""
import requests

if __name__ == "__main":
    response = request.get("https://intranet.hbtn.io/status")
    body = response.text

    print("body response:")
    print("\t- type: {}".format(type(vody)))
    print("\t- content: {}".format(body))
