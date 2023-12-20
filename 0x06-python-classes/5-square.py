#!/usr/bin/python3
"""a class Square."""


class Square:
    """it is representing a square."""

    def __init__(self, size):
        """it Initializes a square.
        Args:
        size int : The size of square
        Returns:
        it returns nothing
        """
        self.size = size

    @property
    def size(self):
        """it sets new size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """it always return the current area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print out the square with the # character"""
        if self.__size == 0:
            print("")
        else:
            j = 0
            i = 0
            for s in range(self.__size):
                for k in range(self.__size):
                    print("#", end="")
                print()
