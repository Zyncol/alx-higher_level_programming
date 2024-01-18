#!/usr/bin/python3
""" 
class square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class square inheriting from rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        class constructor for the clas
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """
        representation of square
        """
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x, self.y, self.size)
      @property
    def size(self):
        """
        retrieving the size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        sets width and height of the same value
        """
        self.width = value
        self.height = value

