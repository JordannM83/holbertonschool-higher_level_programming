#!/usr/bin/python3
"""
This module contains a Rectangle class that inherits from BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A Rectangle class that inherits from BaseGeometry.

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
