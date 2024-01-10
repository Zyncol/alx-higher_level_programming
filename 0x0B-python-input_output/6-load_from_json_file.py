#!/usr/bin/python3
"""
load_from_json_file.py
"""
import json


def load_from_json_file(filename):
    """Creating an Object from a “JSON file”
    Args:
        filename: name of JSON file to decode
    Return:
    object decoded from filename
    """
    with open(filename, "r", encoding="utf-8") as fil:
        ob = json.load(fil)

    return ob
