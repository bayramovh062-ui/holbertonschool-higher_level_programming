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
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
