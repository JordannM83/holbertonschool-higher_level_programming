#!/usr/bin/python3
"""
This module contains a class MyList that inherits from list
and provides additional functionality for printing sorted lists.
"""


class MyList(list):
    """
    A class that inherits from list and adds a print_sorted method.

    This class extends the built-in list class to provide
    functionality for printing the list in sorted order.
    """

    def print_sorted(self):
        """
        Prints the list, but sorted (ascending sort).

        Assumes that all elements of the list will be of type int.
        Does not modify the original list.
        """
        print(sorted(self))
