#!/usr/bin/python3
"""
Module that adds 2 integers
"""

def parse_int(num):
    try:
        return int(num)
    except (TypeError, ValueError):
        return -1


def add_integer(a, b=98):
    """Add two integers.

    Args:
        a: first integer
        b: second integer (default: 98)

    Returns:
        The addition of a and b

    Raises:
        TypeError: if a or b is not an integer or float
    """
    if parse_int(a) == -1:
        raise TypeError("a must be an integer")
    elif parse_int(b) == -1:
        raise TypeError("b must be an integer")
    else:
        return int(a + b)
