#!/bin/bash
# send a GET request and display the body of the response
curl -s -d "X-School-User-Id: 98" "$1"
