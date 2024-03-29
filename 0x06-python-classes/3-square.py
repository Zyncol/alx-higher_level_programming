#!/usr/bin/python3
"""a class Square"""


class Square:
    """for the  square."""
    def __init__(self, size=0):
        """a new square
        Args:
            size int: The size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns  current area of the square"""
        return (self.__size ** 2)
