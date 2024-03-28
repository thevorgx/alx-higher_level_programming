#!/bin/bash
# display all HTTP methods the server will accept
curl -s -L -X OPTIONS "$1"
