#!/usr/bin/python3
"""a base geometry class BaseGeometry."""


class BaseGeometry:
    """
    for the geometry
    """
    def area(self):
        """
        not to be implemented yet
        """
        raise Exception("area() is not implemented yet")

    def integer_validator(self, name, value):
        """
        checks the value
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
