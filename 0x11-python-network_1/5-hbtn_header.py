#!/usr/bin/python3
"""Display X-Request-Id header variable of a request to a given URL
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    reque = requests.get(url)
    print(reque.headers.get("X-Request-Id"))
