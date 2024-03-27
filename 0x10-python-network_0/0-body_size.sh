#!/bin/bash
# script that takes in a URL, sends a request to that URL, and displays the size of the body of the response in bytes
curl -sI "$1" | grep -i Content-Length | cut -d " " -f 2
