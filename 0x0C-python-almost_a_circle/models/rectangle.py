#!/usr/bin/python3
"""class Rectangle inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """class inheriting from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def height(self):
        """
        retrieves the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the height
        """
        try:
            assert isinstance(value, int)
        except BaseException:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def width(self):
        """
        retrieves the  width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setting the width
        """
        try:
            assert isinstance(value, int)
        except BaseException:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value


    @property
    def y(self):
        """
        checks and retrieves y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        setting the y
        """
        try:
            assert isinstance(value, int)
        except BaseException:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @property
    def x(self):
        """
        retrieves the digit  x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        setting x
        """
        try:
            assert isinstance(value, int)
        except BaseException:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    def area(self):
        """
        Return: 
            the area of rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        prints rectangle using # character
        """
        for ine in range(self.__y):
            print()
        for oi in range(self.__height):
            for mpata in range(self.__x):
                print(" ", end="")
            for ko in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """str method to return rectangle representation"""
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id,
                                                       self.__x,
                                                       self.__y,
                                                       self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """assigns an argument to each list"""
        if (args):
            for oi, ko in enumerate(args):
                if oi == 0:
                    self.id = ko
                elif oi == 1:
                    self.width = ko
                elif oi == 2:
                    self.height = ko
                elif oi == 3:
                    self.x = ko
                elif oi == 4:
                    self.y = ko
        for ikey, ivalue in kwargs.items():
            setattr(self, ikey, ivalue)

    def to_dictionary(self):
        """returns dictionary representation of rectangle"""
        my_dict = {}
        my_dict["id"] = self.id
        my_dict["width"] = self.width
        my_dict["height"] = self.height
        my_dict["x"] = self.x
        my_dict["y"] = self.y
        return my_dict
