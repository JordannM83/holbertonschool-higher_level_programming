#!/usr/bin/python3
"""
This module contains a VerboseList class that extends the built-in list
with notification messages for list operations.
"""


class VerboseList(list):
    """
    A list subclass that prints notifications when items are added or removed.
    
    This class extends the built-in list class and overrides methods
    to provide verbose output about list operations.
    """
    
    def append(self, item):
        """
        Add an item to the end of the list with a notification.
        
        Args:
            item: The item to add to the list
        """
        super().append(item)
        print(f"Added [{item}] to the list.")
    
    def extend(self, iterable):
        """
        Extend the list with items from an iterable with a notification.
        
        Args:
            iterable: An iterable containing items to add to the list
        """
        items_count = len(list(iterable))
        super().extend(iterable)
        print(f"Extended the list with [{items_count}] items.")
    
    def remove(self, item):
        """
        Remove an item from the list with a notification.
        
        Args:
            item: The item to remove from the list
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)
    
    def pop(self, index=-1):
        """
        Remove and return an item from the list with a notification.
        
        Args:
            index (int): The index of the item to remove (default: -1, last item)
            
        Returns:
            The item that was removed from the list
        """
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)