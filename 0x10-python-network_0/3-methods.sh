#!/bin/bash
# display all HTTP methods the server will accept
curl -s -I -X OPTIONS "$1" | awk '/Allow/ {print}'
