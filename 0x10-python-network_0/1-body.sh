#!/bin/bash
# Takes in a URL, sends a GET request to the URL, displays the body of the response
curl -sLX GET "$1"
