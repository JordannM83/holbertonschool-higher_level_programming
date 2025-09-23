#!/usr/bin/python3
"""
Test file for task_04_flyingfish module demonstrating multiple inheritance.
"""

from task_04_flyingfish import Fish, Bird, FlyingFish

if __name__ == "__main__":
    # Test Fish class
    print("=== Testing Fish ===")
    fish = Fish()
    fish.swim()
    fish.habitat()
    
    print("\n=== Testing Bird ===")
    bird = Bird()
    bird.fly()
    bird.habitat()
    
    print("\n=== Testing FlyingFish ===")
    flying_fish = FlyingFish()
    flying_fish.fly()
    flying_fish.swim()
    flying_fish.habitat()
    
    print("\n=== Method Resolution Order ===")
    print("FlyingFish MRO:", FlyingFish.__mro__)
    
    print("\n=== Inheritance Check ===")
    print("Is FlyingFish a Fish?", isinstance(flying_fish, Fish))
    print("Is FlyingFish a Bird?", isinstance(flying_fish, Bird))
    print("Is FlyingFish a FlyingFish?", isinstance(flying_fish, FlyingFish))