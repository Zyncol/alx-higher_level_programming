#!/usr/bin/python3
"""
save_to_json_file.py
"""
import json


def save_to_json_file(my_obj, filename):
    """writing an object to afile, using a JSON representation
    Args:
        my_obj: py object to write to file
        filename: name of the file
    Return:
        none
    """
    with open(filename, 'w', encoding="utf-8") as fil:
        json.dump(my_obj, fil)
