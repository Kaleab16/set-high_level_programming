#!/bin/bash
# Sends an OPTIONS request and prints the Allow header's methods.
curl -s -X OPTIONS -I "$1" | grep -i "Allow" | cut -d' ' -f2-
