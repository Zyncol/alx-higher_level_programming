#!/bin/bash
# Display accepted request by server
curl -sI "$1" | grep "Allow" | cut -d" " -f 2-
