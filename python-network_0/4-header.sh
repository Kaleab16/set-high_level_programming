#!/bin/bash
# Sends a GET request with a custom X-School-User-Id header.
curl -s -H "X-School-User-Id: 98" "$1"
