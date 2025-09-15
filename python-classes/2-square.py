#!/usr/bin/python3
"""
This module defines a Square class with size validation.

The Square class represents a square geometric figure with proper
size validation to ensure data integrity.
"""


class Square:
    """A class that defines a square.
    This is an empty class that serves as the foundation for building
    a more complete Square class in future iterations.
    """
    __size = None

    def __init__(self, size=0):
        if not isinstance(size, (int)):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
