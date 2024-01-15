#!/usr/bin/python3
"""class Rectangle inherits fro the Base"""
from models.base import Base


class Rectangle(Base):
    """class inheriting from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor with attri"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
