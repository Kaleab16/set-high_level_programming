#!/bin/bash
# Sends a request and displays only the HTTP status code, no pipes.
curl -s -o /dev/null -w "%{http_code}" "$1"
