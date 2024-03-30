#!/bin/bash
# a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
#The size must be displayed in bytes
#You have to use curl
#Please test your script in the sandbox provided, using the web server running on port 5000

if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

URL=$1

# Send a request using curl and store the response in a temporary file
TEMP_FILE=$(mktemp)
curl -sS -o "$TEMP_FILE" "$URL"

# Check if curl request was successful
if [ $? -ne 0 ]; then
    echo "Error: Failed to retrieve data from $URL"
    exit 1
fi

# Get the size of the response body in bytes
SIZE=$(wc -c < "$TEMP_FILE")

# Display the size in bytes
echo "Size of response body from $URL: $SIZE bytes"

# Clean up the temporary file
rm "$TEMP_FILE"

