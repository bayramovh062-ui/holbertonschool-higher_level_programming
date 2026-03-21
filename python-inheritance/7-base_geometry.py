#!/usr/bin/python3
"""
This module contains the BaseGeometry class.
"""


class BaseGeometry:
    """
    A base geometry class.
    """

    def area(self):
        """
        Raises an Exception indicating area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        this function checks value
        """
        if value is not int:
            raise TypeError("{self.name} must be an integer")
        if value <= 0:
            raise TypeError("{self.name} must be greater than 0")
