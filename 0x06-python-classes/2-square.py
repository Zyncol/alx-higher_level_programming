#!/usr/bin/python3
"""a class Square."""


class Square:
    """representing a square."""
    def __init__(self, size=0):
        """Initialising
        Args:
            size int: The size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
