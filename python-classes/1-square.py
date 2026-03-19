#!/usr/bin/python3
"""
This module defines a Square class.
"""


class Square:
    """
    Square class represents a geometric square shape.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size: The size of the square (no type/value verification yet).
        """
        self.__size = size
