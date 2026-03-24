#!/usr/bin/python3
"""
this module about abstracts withs shapes examples
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    this class an abstract class and
    it require two abstract methods aboyt shape
    """
    @abstractmethod
    def perimeter(self):
        """
        this is first abstract function for perimeter
        """
        pass

    @abstractmethod
    def area(self):
        """
        this is second abstract function for area
        """
        pass


class Circle(Shape):
    """
    this class for circle's parametrs
    """
    def __init__(self, radius):
        """
        this function initalization radius
        """
        self.radius = radius

    def perimeter(self):
        """
        this is perimeter function for Circle
        """
        return 2 * math.pi * self.radius

    def area(self):
        """
        this is area function for Circle
        """
        return math.pi * (self.radius ** 2)


class Rectangle(Shape):
    """
    this class for Rectangle's paramters
    """
    def __init__(self, width, height):
        """
        this function initalizations width and height
        """
        self.width = width
        self.height = height

    def perimeter(self):
        """
        this is perimeter for Rectangle
        """
        return 2 * (self.width + self.height)

    def area(self):
        """
        this is area for Rectangle
        """
        return self.width * self.height


def shape_info(figure):
    """
    this function prints figure's information
    """
    print(f"Area: {figure.area()}")
    print(f"Perimeter: {figure.perimeter()}")
