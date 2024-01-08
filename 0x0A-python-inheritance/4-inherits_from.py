#!/usr/bin/python3
"""
checking class
"""


def inherits_from(obj, a_class):
    if isinstance(type(obj), a_class) and type(obj) != a_class:
        return True
    elif isinstance(type(obj), a_class) and type(obj) == a_class:
        return False
