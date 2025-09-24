#!/usr/bin/python3
"""
This module demonstrates multiple inheritance with Fish, Bird, and FlyingFish
classes.
"""


class Fish:
    """
    Fish class with swimming and habitat methods.
    """

    def swim(self):
        """
        Method for fish swimming behavior.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Method describing fish habitat.
        """
        print("The fish lives in water")


class Bird:
    """
    Bird class with flying and habitat methods.
    """

    def fly(self):
        """
        Method for bird flying behavior.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Method describing bird habitat.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    FlyingFish class that inherits from both Fish and Bird.

    This class demonstrates multiple inheritance and method resolution order.
    """

    def fly(self):
        """
        Override the fly method for flying fish.
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Override the swim method for flying fish.
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Override the habitat method for flying fish.
        """
        print("The flying fish lives both in water and the sky!")
