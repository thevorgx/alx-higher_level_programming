#!/bin/bash
# display the body of the response only if status code is 200
[ "$(curl -o /dev/null -s -w "%{http_code}" "$1")" -eq 403 ] && curl -sL "$1"
