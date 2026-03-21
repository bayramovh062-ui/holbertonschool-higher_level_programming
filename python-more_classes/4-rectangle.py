#!/usr/bin/python3
"""
that is rectangle module
"""


class Rectangle:
    """
    rectangle represents a rectangle
    """

    def __init__(self, width=0, height=0):
        """
        we can initialize object of this class
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
        returns the rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        returns the rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        returns string representation of the rectangle with #
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        
        # Hər sətrində en qədər '#' olan, uzunluq qədər sətir yaradırıq
        rectangle_str = []
        for i in range(self.__height):
            rectangle_str.append("#" * self.__width)
        
        # Sətirləri 'yeni sətir' (newline) ilə birləşdirib qaytarırıq
        return "\n".join(rectangle_str)

    def __repr__(self):
        """
        this function returns a string that you can create a
        new rectangle with its result
        """
        return f'Renctangle({self.__width}, {self.__height})'
