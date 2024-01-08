#!/usr/bin/python3
"""
Return:
the list of available attributes and methods of an object
"""


def lookup(obj):
    """
    Return:
           list of attributes
    arg:
        obj: object to be looked
    """
    return (dir(obj))
