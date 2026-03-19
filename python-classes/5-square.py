#!/usr/bin/python3
"""
This module defines a Square class with getter and setter.
"""


class Square:
    """
    Square class represents a geometric square shape.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.
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
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Returns the current square area.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints in stdout the square with the character #
        """
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                print("#" * self.size)
