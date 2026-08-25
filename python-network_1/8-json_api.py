#!/usr/bin/python3
"""POSTs a letter to search_user and displays JSON results or errors."""
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    url = "http://127.0.0.1:5000/search_user"
    response = requests.post(url, data={"q": q})

    try:
        result = response.json()
    except ValueError:
        print("Not a valid JSON")
    else:
        if not result:
            print("No result")
        else:
            print("[{}] {}".format(result.get("id"), result.get("name")))
