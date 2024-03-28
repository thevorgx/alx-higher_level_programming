#!/bin/bash
# display the body of the response only if status code is 200
if [ "$http_code" -eq 200 ]; then curl -sL "$1"; fi
