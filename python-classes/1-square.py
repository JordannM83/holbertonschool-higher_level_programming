#!/usr/bin/python3
"""
This module defines a Square class with a private size attribute.

The Square class represents a square geometric figure with a size attribute.
"""


class Square:
    """A class that defines a square.
    This is an empty class that serves as the foundation for building
    a more complete Square class in future iterations.
    """
    __size = None

    def __init__(self, new_size=None):
        self.__size = new_size
