#!/usr/bin/python3
"""
checks a function
"""


def is_same_class(obj, a_class):
    """
    checks if object == class
    arg:
        obj : the object to be checked
        a_class : type
    Return:
        object if true 
        otherwise false
    """
    if type(obj) == a_class:
        return True
    elif type(obj) != a_class:
        return False
