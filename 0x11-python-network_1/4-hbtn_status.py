#!/usr/bin/python3
"""Python script that fetch https://alx-intranet.hbtn.io/status"""
if __name__ == "__main__":
    import requests

    reque = requests.get("https://alx-intranet.hbtn.io/status")
    print('Body response:\n\t- type: {}\n\t- content: {}'
          .format(type(reque.text), reque.text))
