#!/bin/bash
#a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response
curl -sI "$1" | grep -i Allow | cut -d " " -f2-
