#!/usr/bin/python3
"""
This module demonstrates duck typing with abstract Shape classes.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for shapes.

    Defines the interface that all shape subclasses must implement.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method to calculate the area of the shape.

        Returns:
            float: The area of the shape
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to calculate the perimeter of the shape.

        Returns:
            float: The perimeter of the shape
        """
        pass


class Circle(Shape):
    """
    Circle class that inherits from Shape.

    Implements area and perimeter methods for a circle.
    """

    def __init__(self, radius):
        """
        Initialize a Circle with a given radius.

        Args:
            radius (float): The radius of the circle
        """
        self.radius = radius

    def area(self):
        """
        Calculate the area of the circle.

        Returns:
            float: The area of the circle (π * r²)
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Calculate the perimeter of the circle.

        Returns:
            float: The perimeter of the circle (2 * π * r)
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle class that inherits from Shape.

    Implements area and perimeter methods for a rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle with given width and height.

        Args:
            width (float): The width of the rectangle
            height (float): The height of the rectangle
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            float: The area of the rectangle (width * height)
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle (2 * (width + height))
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print the area and perimeter of a shape using duck typing.

    This function doesn't check the type of the shape object,
    it trusts that the object implements the Shape interface.

    Args:
        shape: An object that implements area() and perimeter() methods
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
