#!/bin/bash
# Sends a DELETE request to the URL passed as the first argument
# Displays the body of the response
curl -sLX DELETE "$1"
