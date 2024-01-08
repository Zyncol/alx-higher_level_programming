#!/usr/bin/python3
"""
a function that adds attributes to objects
"""


def add_attribute(obj, att, value):
    """Adds a new attribute to an object
    Args:
        obj: object to add an attribute to.
        att: name of attribute to add to obj.
        value: value of att.
    Raise:
        TypeError: If the it cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
