#!/usr/bin/python3
"""takes in a URL, sends a request to the URL"""
import urllib.request as request
from sys import argv


if __name__ == "__main__":
    pempho = request.Request(argv[1])
    with request.urlopen(pempho) as reques:
        print(reques.headers.get('X-Request-Id'))
