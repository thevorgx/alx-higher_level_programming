#!/bin/bash
# send a DELETE request to the URL passed as the first argument and display the body of the response
curl -X DELETE "$1"
