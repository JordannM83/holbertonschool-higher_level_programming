#!/usr/bin/python3
"""
This module contains a BaseGeometry class with an area method.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class with Basegeometry like parent
    this sub class is rectangle
    """
    def __init__(self, width, height):
        """
        this module is the initilisation of rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        return f"[{type(self).__name__}] {self.__width}/{self.__height}"

    def area(self):
        return self.__width * self.__height
