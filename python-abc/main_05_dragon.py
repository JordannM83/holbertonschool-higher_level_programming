#!/usr/bin/python3
"""
Test file for task_05_dragon module demonstrating mixin classes.
"""

from task_05_dragon import SwimMixin, FlyMixin, Dragon

if __name__ == "__main__":
    print("=== Testing SwimMixin ===")
    # Can't instantiate mixin directly in a meaningful way, but we can test it
    
    print("=== Testing FlyMixin ===")
    # Can't instantiate mixin directly in a meaningful way, but we can test it
    
    print("=== Testing Dragon with Mixins ===")
    dragon = Dragon("Draco")
    print(f"Dragon name: {dragon.name}")
    
    # Test dragon's own methods
    dragon.roar()
    
    # Test methods from mixins
    dragon.swim()  # From SwimMixin
    dragon.fly()   # From FlyMixin
    
    print("\n=== Method Resolution Order ===")
    print("Dragon MRO:", Dragon.__mro__)
    
    print("\n=== Inheritance Check ===")
    print("Is Dragon a SwimMixin?", isinstance(dragon, SwimMixin))
    print("Is Dragon a FlyMixin?", isinstance(dragon, FlyMixin))
    print("Is Dragon a Dragon?", isinstance(dragon, Dragon))
    
    print("\n=== Mixin Pattern Demonstration ===")
    print("Dragon has swim method:", hasattr(dragon, 'swim'))
    print("Dragon has fly method:", hasattr(dragon, 'fly'))
    print("Dragon has roar method:", hasattr(dragon, 'roar'))