#!/usr/bin/python3
"""
class_to_json Module
"""


def class_to_json(obj):
    """
    Return:
        a disctionary with simple
        data structures
    Args:
        obj: an instance of a Class
    """
    return vars(obj)
