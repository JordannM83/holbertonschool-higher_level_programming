#!/usr/bin/python3
"""
This module contains a CountedIterator class that extends iterator
functionality to keep track of the number of items iterated.
"""


class CountedIterator:
    """
    An iterator that keeps track of the number of items iterated.

    This class wraps around an iterator and counts how many items
    have been fetched using the __next__ method.
    """

    def __init__(self, iterable):
        """
        Initialize the CountedIterator with an iterable.

        Args:
            iterable: Any iterable object (list, tuple, string, etc.)
        """
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """
        Get the current count of items that have been iterated.

        Returns:
            int: The number of items that have been fetched
        """
        return self.count

    def __next__(self):
        """
        Get the next item from the iterator and increment the counter.

        Returns:
            The next item from the iterator

        Raises:
            StopIteration: When there are no more items to iterate
        """
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    def __iter__(self):
        """
        Return the iterator object itself.

        Returns:
            CountedIterator: The iterator object
        """
        return self
