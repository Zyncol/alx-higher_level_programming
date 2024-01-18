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
        return '[Square] ({}) {}/{} - {}'.format(self.id,
                                                 self.x,
                                                 self.y, self.size)

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

    def update(self, *args, **kwargs):
        """
        assigning the attributes
        """
        if args:
            j = 0
            while j < len(args):
                if j == 0:
                    self.id = args[j]
                elif j == 1:
                    self.size = args[j]
                elif j == 2:
                    self.x = args[j]
                elif j == 3:
                    self.y = args[j]
                j++
        for key, value in kwargs.items():
            setattr(self, key, value)
