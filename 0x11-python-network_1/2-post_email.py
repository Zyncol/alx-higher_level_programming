#!/usr/bin/python3
"""Sends POST request to a given URL with a given email
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    valu = {"email": sys.argv[2]}
    dat = urllib.parse.urlencode(valu).encode("ascii")

    request = urllib.request.Request(url, dat)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
