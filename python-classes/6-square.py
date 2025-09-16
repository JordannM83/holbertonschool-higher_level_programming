#!/usr/bin/python3
"""
This module defines a Square class with position and printing functionality.

The Square class represents a square geometric figure with the ability
to be positioned and printed using the '#' character.
"""
"""
Module defining the Square class, which allows creation and
manipulation of squares with a specific size and position.
The Square class provides methods to calculate area and print
the square with custom positioning using the '#' character.
"""


class Square:
    """
    Represents a square with a given size and position.
    Provides methods to calculate the area and print the square
    with custom formatting.
    The position allows the square to be printed with an offset in the console.
    """
    __size = None
    __position = None

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
        """
        Initialize a Square instance with a given size and position.
        Size must be an integer >= 0. Position must
        be a tuple of 2 positive integers.
        Raises TypeError or ValueError if arguments are invalid.
        """

    @property
    def size(self):
        return self.__size
        """
        Get the current size of the square.
        Returns the size as an integer.
        """

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
        """
        Set the size of the square.
        Value must be an integer >= 0. Raises TypeError
        or ValueError if invalid.
        """

    def area(self):
        return (self.__size * self.__size)
        """
        Calculate and return the area of the square.
        Returns the area as an integer.
        """

    @property
    def position(self):
        return self.__position
        """
        Get the current position of the square.
        Returns the position as a tuple of two positive integers.
        """

    @position.setter
    def position(self, value):
        if (not isinstance(value, (tuple, list)) or isinstance(value[0], int)
           or isinstance(value[1], int) or value[0] < 0
           or value[1] < 0 or len(value) < 1):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
        """
        Set the position of the square.
        Value must be a tuple of two positive integers.
        Raises TypeError if invalid.
        """

    def my_print(self):
        if self.__position[0] > 0:
            for i in range(self.__position[1]):
                print()
        if self.size == 0:
            print("")
        else:
            for i in range(0, self.size):
                for k in range(0, self.position[0]):
                    print(" ", end="")
                for j in range(0, self.size):
                    print("#", end="")
                print("")
        """
        Print the square using the '#' character,
        with the specified position offset.
        If size is 0, prints an empty line.
        Position controls the indentation and vertical offset.
        """
