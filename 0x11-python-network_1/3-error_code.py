#!/usr/bin/python3
"""sends a request to the URL"""
import urllib.error as error
import urllib.request as request
from sys import argv


if __name__ == "__main__":
    reque = request.Request(argv[1])
    try:
        with request.urlopen(reque) as r:
            print(r.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
