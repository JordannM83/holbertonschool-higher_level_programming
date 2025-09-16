#!/usr/bin/python3
"""
This module defines a Square class with position and printing functionality.

The Square class represents a square geometric figure with the ability
to be positioned and printed using the '#' character.
"""


class Square:
    """A class that defines a square.
    This is an empty class that serves as the foundation for building
    a more complete Square class in future iterations.
    """
    __size = None
    __position = None

    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if (not isinstance(position, tuple) or position[0] < 0 or
           position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, int) or value < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        if self.__position[0] > 0:
            for i in range(self.__position[0]):
                print()
        if self.size == 0:
            print("")
        else:
            for i in range(0, self.size):
                for k in range(0, self.position[1]):
                    print(" ", end="")
                for j in range(0, self.size):
                    print("#", end="")
                print("")
