#!/bin/bash
# display all HTTP methods the server will accept
curl -s -I "$1" | awk '/Allow/ {print}'
