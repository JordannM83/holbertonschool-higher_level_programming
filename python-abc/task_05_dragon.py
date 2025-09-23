#!/usr/bin/python3
"""
This module demonstrates mixin classes with SwimMixin, FlyMixin, and Dragon.
"""


class SwimMixin:
    """
    Mixin class that provides swimming functionality.
    """
    
    def swim(self):
        """
        Method for swimming behavior.
        """
        print("The creature swims!")


class FlyMixin:
    """
    Mixin class that provides flying functionality.
    """
    
    def fly(self):
        """
        Method for flying behavior.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class that uses mixin classes for composition.
    
    This class demonstrates how mixins can be used to compose functionality
    rather than using traditional inheritance.
    """
    
    def __init__(self, name):
        """
        Initialize a Dragon with a name.
        
        Args:
            name (str): The name of the dragon
        """
        self.name = name
    
    def roar(self):
        """
        Dragon's roaring behavior.
        """
        print("The dragon roars!")