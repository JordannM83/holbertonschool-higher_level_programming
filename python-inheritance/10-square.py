#!/usr/bin/python3

"""
create a subclass square from rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Write a class Square that inherits from Rectangle
    """
    def __init__(self, size):
        """
        this module is the initilisation of square
        """
        self.integer_validator("size", size)
        self.__size = size
        self.__width = size
        self.__height = size