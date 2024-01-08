#!/usr/bin/python3
"""
checking class
"""


def inherits_from(obj, a_class):
    """
    evaluates an obj
    arg:
        obj: object to be looked
        a_class: type
    Return:
        False or true
    """
    if isinstance(type(obj), a_class) and type(obj) != a_class:
        return True
    elif isinstance(type(obj), a_class) and type(obj) == a_class:
        return False
