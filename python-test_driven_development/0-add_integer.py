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
    if (isinstance(a, float) and a != a) or (isinstance(b, float) and b != b):
        raise ValueError("cannot convert float NaN to integer")

    if (isinstance(a, float) and (a == float('inf') or
                                  a == float('-inf'))) or \
       (isinstance(b, float) and (b == float('inf') or b == float('-inf'))):
        raise OverflowError("cannot convert float infinity to integer")

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
