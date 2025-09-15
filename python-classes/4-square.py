#!/usr/bin/python3
"""
This module defines a Square class with getter and setter properties.

The Square class represents a square geometric figure with proper
size validation using property decorators for controlled access.
"""


class Square:
    """A class that defines a square.
    This is an empty class that serves as the foundation for building
    a more complete Square class in future iterations.
    """
    __size = None

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return (self.__size * self.__size)
