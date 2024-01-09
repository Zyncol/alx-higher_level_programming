#!/usr/bin/python3
"""
from_json_string.py
"""
import json


def from_json_string(my_str):
    """
    Return:
        an object represented by a JSON string
    """
    return json.loads(my_str)
