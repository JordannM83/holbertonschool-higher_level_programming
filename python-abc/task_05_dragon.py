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

    def roar(self):
        """
        Dragon's roaring behavior.
        """
        print("The dragon roars!")

class draco(Dragon):
    """
    Classe draco héritant de Dragon pour tester les capacités et le MRO.
    """
    def ability(self):
        """
        tester les compétences
        """
        print("fly():", self.fly())
        print("swim():", self.swim())
        print("roar():", self.roar())
        print(draco.mro())

if __name__ == "__main__":
    new_draco = draco()
    new_draco.ability()