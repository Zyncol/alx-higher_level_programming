#!/usr/bin/python3
"""
Returns:
    true os false
"""


def is_kind_of_class(obj, a_class):
    """
    find a class inherited form a class
    arg:
        obj : object to be looked
        a_class: type
    Return:
        true or false
    """
    return isinstance(obj, a_class)
