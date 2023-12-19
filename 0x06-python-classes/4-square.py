#!/usr/bin/python3
"""a class Square"""


class Square:
    """representing a square"""
    def __init__(self, size=0):
        """Initializing  square
        Args:
            size int: The size of the new square.
        """
        self.__size = size

    @property
    def size(self):
        """sets the current size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returnd the current area"""
        return (self.__size ** 2)
