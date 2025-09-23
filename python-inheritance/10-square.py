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
        super().__init__(size, size)

    def __str__(self):
        return (f"[Rectangle] {self._Rectangle__width}/"
                f"{self._Rectangle__height}")
