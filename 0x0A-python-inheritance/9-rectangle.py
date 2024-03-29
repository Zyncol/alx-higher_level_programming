#!/usr/bin/python3
"""
Creates a Rectangle class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    a rectangle
    Attributes:
            width: for the width
            height: for the height
    """
    def __init__(self, width, height):
        """
        initialises
        arg:
            width: for width
            height: for height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """"return: the string"""
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """returns area"""
        return self.__width * self.__height
