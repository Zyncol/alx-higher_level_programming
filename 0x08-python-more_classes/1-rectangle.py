#!/usr/bin/python3
"""task 1-rectangle
a Rectangle class modified
"""


class Rectangle:
    """Rectangle class width and height defined"""

    def __init__(self, width=0, height=0):
        """Initializing a rectangle instance
            width: width of the rectangle side
            height: height of the rectangle side
        """
        self.width = width
        self.height = height

        @property
    def height(self):
        """a rectangle instance height is set"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setting the height
            value: it must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

        @property
    def width(self):
        """the width of a Rectangle instance."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting the width
            value:it must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
