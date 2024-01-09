#!/usr/bin/python3
"""a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    its a rectange
    Attributes:
            height: for the height
            width: for the width
    """
    def __init__(self, width, height):
        """
        initialises
        arg:
            width: fro the width
            height: for the hieght
        """
        self.integer_validator("height", height)
        self.__height = height
        self.integer_validator("width", width)
        self.__width = width
