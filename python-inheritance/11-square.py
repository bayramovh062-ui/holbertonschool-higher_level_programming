#!/usr/bin/python3
"""
This module contains a class Square that inherits from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A representation of a square.
    """

    def __init__(self, size):
        """
        Instantiation of the square with size.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Returns the area of the square.
        """
        return self.__size * self.__size

    def __str__(self):
        """
        returns right string format
        """
        return f"[square] {self.size}/{self.size}"
