#!/bin/bash
#a Bash script that takes sends a request to the URL
curl -sI "$1" | grep "Content-Length" | cut -d ' ' -f 2
