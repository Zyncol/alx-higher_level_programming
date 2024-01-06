#!/usr/bin/python3
"""task 3-rectangle
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

    def __str__(self):
        """Return:
        an informal and nicely printable string representation
        of rectangle,in '#' character
        """
        if self.__height == 0 or self.__width == 0:
            return ''
        strd = ''
        for k in range(self.__height):
            for j in range(self.__width):
                strd += '#'
            strd += '\n'
        return strd[:-1]

    def __repr__(self):
        """Return:
        a string representation of a Rectangle instance
        capable of create another using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Deleting a rectangle"""
        print("Bye rectangle...")

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

    def area(self):
        """Calculates the area of a rectangle
        Return:
            Area of the the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of rectangle
        Return: Perimeter of the rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
