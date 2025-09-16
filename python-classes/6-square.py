#!/usr/bin/python3
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

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a Square instance with a given size and position.
        Size must be an integer >= 0. Position must
        be a tuple of 2 positive integers.
        Raises TypeError or ValueError if arguments are invalid.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        Get the current size of the square.
        Returns the size as an integer.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.
        Value must be an integer >= 0. Raises TypeError
        or ValueError if invalid.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculate and return the area of the square.
        Returns the area as an integer.
        """
        return (self.__size * self.__size)

    @property
    def position(self):
        """
        Get the current position of the square.
        Returns the position as a tuple of two positive integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square.
        Value must be a tuple of two positive integers.
        Raises TypeError if invalid.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
           not isinstance(value[0], int) or not isinstance(value[1], int)
           or value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """
        Print the square using the '#' character,
        with the specified position offset.
        If size is 0, prints an empty line.
        Position controls the indentation and vertical offset.
        """
        if self.size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(0, self.size):
                for k in range(0, self.position[0]):
                    print(" ", end="")
                for j in range(0, self.size):
                    print("#", end="")
                print("")
