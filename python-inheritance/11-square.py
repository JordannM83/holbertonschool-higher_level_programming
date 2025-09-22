#!/usr/bin/python3
"""
This module contains a Square class that inherits from Rectangle
with proper string representation.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A Square class that inherits from Rectangle with square
    string representation.

    This class represents a square, which is a special case of a rectangle
    where width and height are equal.
    """

    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square (must be positive integer)
        """
        pass

    def __str__(self):
        """
        Returns the string representation of the square.

        Returns:
            str: Square description in format [Square] <size>/<size>
        """
        pass
