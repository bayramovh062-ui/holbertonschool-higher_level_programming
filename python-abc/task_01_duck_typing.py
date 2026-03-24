#!/usr/bin/env python3
"""
Shapes, Interfaces, and Duck Typing module.
"""
import math 
from abc import ABC, abstractmethod


class Shape(ABC):
    """Shape abstract class."""

    @abstractmethod
    def area(self):
        """Returns the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Returns the perimeter of the shape."""
        pass


class Circle(Shape):
    """Circle class."""

    def __init__(self, radius):
        """Initializes a Circle."""
        self.radius = radius

    def area(self):
        """Calculates Circle area."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculates Circle perimeter."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class."""

    def __init__(self, width, height):
        """Initializes a Rectangle."""
        self.width = width
        self.height = height

    def area(self):
        """Calculates Rectangle area."""
        return self.width * self.height

    def perimeter(self):
        """Calculates Rectangle perimeter."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Prints the area and perimeter of a shape."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
