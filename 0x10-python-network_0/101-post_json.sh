#!/bin/bash
#This script sendss
curl -s "$1" -X POST -H "Content-Type: application/json" -d "$(cat "$2")"
