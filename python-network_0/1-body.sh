#!/bin/bash
# Sends a GET request to the URL and prints the body only if status is 200.
[ "$(curl -s -o /dev/null -w "%{http_code}" "$1")" = "200" ] && curl -s "$1"
