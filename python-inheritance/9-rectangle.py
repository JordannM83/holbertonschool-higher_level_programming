#!/usr/bin/python3
"""
This module contains a Rectangle class that inherits from BaseGeometry
with implemented area method and string representation.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A Rectangle class that inherits from BaseGeometry with area implementation.

    This class represents a rectangle with width and height,
    validated using the integer_validator method from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle (must be positive integer)
            height (int): The height of the rectangle
            (must be positive integer)
        """
        pass

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height)
        """
        pass

    def __str__(self):
        """
        Returns the string representation of the rectangle.

        Returns:
            str: Rectangle description in format [Rectangle] <width>/<height>
        """
        pass
