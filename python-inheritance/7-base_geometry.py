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

    def integer_validator(self, name, value):
        """
        Public instance method: def integer_validator(self, name, value):
        that validates value:
        you can assume name is always a string
        if value is not an integer: raise a TypeError exception,
        with the message <name> must be an integer
        if value is less or equal to 0: raise a ValueError
        exception with the message
        <name> must be greater than 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
