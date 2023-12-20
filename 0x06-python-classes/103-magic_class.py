#!/usr/bin/python3
"""a MagicClass matching"""
import math


class MagicClass:
    """representing  circle."""

    def __init__(self, radius=0):
        """Initializes MagicClass.

        Arg:
            radius (float or int): The radius of MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("the radius should be a number")
        self.__radius = radius

    def area(self):
        """
        it returns the area of the MagicClass
        """
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """
        it return the circumference of MagicClass
        """
        return (2 * math.pi * self.__radius)
