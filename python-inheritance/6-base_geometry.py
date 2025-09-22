#!/usr/bin/python3
"""
This module contains a BaseGeometry class with an area method.
"""


class BaseGeometry:
    """
    A BaseGeometry class with an area method that raises an Exception.

    This class serves as a base for geometric shapes and operations.
    """

    def area(self):
        """
        Calculates the area of the geometry.

        Raises:
            Exception: Always raises an Exception with the message
                      "area() is not implemented"
        """
        raise Exception("area() is not implemented")
