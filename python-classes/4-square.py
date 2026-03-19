#!/usr/bin/python3
"""
This module defines a Square class.
"""


class Square:
    """
    Square class represents a geometric square shape.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size: The size of the square (no type/value verification yet).
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation.

        Args:
            value (int): The new size to set.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        this function returns area of square
        """
        return self.__size ** 2
