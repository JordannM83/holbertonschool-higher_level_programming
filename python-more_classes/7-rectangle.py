#!/usr/bin/python3
"""
This module defines a Rectangle class with area and perimeter calculations.

The Rectangle class provides private width and height attributes with
validation, and includes methods to calculate the area and perimeter
of the rectangle.
"""


class Rectangle:
    """A class that defines a rectangle with area and perimeter calculations.

    This class represents a rectangle with private width and height attributes
    that includes methods for calculating the geometric properties like
    area and perimeter of the rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle, defaults to 0.
            height (int): The height of the rectangle, defaults to 0.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is negative.
        """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get the width of the rectangle.

        Returns:
            int: The current width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle.

        Returns:
            int: The current height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.height * self.width

    def perimeter(self):
        """Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle, or 0 if width or height is 0.
        """
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return ((self.height + self.width) * 2)

    def __str__(self):
        """
        print the rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            return ((str(self.print_symbol) * self.__width) + ("\n" +
                    str(self.print_symbol) * self.__width)
                    * (self.__height - 1))

    def __repr__(self):
        """
        return a string representation of the rectangle
        to be able to recreate a new instance
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Message when delete an object
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
