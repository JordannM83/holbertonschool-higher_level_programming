#!/usr/bin/python3


"""
Module that adds 2 integers
check if typeerror value error
return sum
"""


"""
this foncion parse a number and return it as an integer,
if it can't be parsed it returns -1
"""


def parse_int(num):
    try:
        return int(num)
    except (TypeError, ValueError):
        return -1


def add_integer(a, b=98):
    """Add two integers.
        a: first integer / b: second integer (default: 98)
    """
    if parse_int(a) == -1:
        raise TypeError("a must be an integer")
    elif parse_int(b) == -1:
        raise TypeError("b must be an integer")
    else:
        return int(a + b)
