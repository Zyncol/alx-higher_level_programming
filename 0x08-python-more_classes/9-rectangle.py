#!/usr/bin/python3
"""task 3-rectangle
a Rectangle class modified
"""


class Rectangle:
    """Rectangle class width and height defined"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializing a rectangle instance
            width: width of the rectangle side
            height: height of the rectangle side
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
                strd += str(self.print_symbol)
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
        Rectangle.number_of_instances -= 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """looks for the biggest triangle based on area
            rect_1: an instance of a rectangle
            rect_2: another instance
        Returns:
            The triangle with the biggest area
            or rect_1 if both rectangles are equal
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2

    @classmethod
    def square(cls, size=0):
        """creating a new rectangle
        size: sizes to be  set to the new rectangle
        Return:
            new rectangle
        """
        return cls(size, size)
