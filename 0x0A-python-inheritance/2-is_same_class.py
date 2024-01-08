#!/usr/bin/python3
"""
checks a function
"""


def is_same_class(obj, a_class):
    if type(obj) == a_class:
        return True
    elif type(obj) != a_class:
        return False
