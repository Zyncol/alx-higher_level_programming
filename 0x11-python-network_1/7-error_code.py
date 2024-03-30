#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    reque = requests.get(url)
    if reque.status_code >= 400:
        print("Error code: {}".format(reque.status_code))
    else:
        print(reque.text)
