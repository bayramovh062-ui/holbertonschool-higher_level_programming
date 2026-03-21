#!/usr/bin/python3
"""
that is rectangle module
"""


class Rectangle:
    """
    rectangle represents a renctangle
    """

    def __init__(self, width=0, height=0):
        """
        we can initalization object of this class
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        this function retrieves width value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        this function sets a value to width variable
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        this function retrieves height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        this function sets a value to height variable
        and checks value
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        this function returns area of rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        this function returns perimeter of rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
