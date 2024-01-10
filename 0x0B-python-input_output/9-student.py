#!/usr/bin/python3
"""
student Module
"""


class Student:
    """
    it defines the class student
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialises the methods
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        retrieves a dictionary of a Student instance
        """
        return vars(self)
