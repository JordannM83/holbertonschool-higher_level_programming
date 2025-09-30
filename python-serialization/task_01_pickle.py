#!/usr/bin/env python3
"""
Pickling custom classes module.

This module demonstrates how to serialize and deserialize custom Python objects
using the pickle module.
"""
import pickle


class CustomObject:
    """
    A custom Python class for demonstration of pickling.

    Attributes:
        name (str): The name of the object
        age (int): The age
        is_student (bool): Whether the object represents a student
    """

    def __init__(self, name, age, is_student):
        """
        Initialize CustomObject.

        Args:
            name (str): The name
            age (int): The age
            is_student (bool): Whether this is a student
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the object's attributes in the specified format.

        Format:
            Name: <name>
            Age: <age>
            Is Student: <is_student>
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance of the object and save it to a file.

        Args:
            filename (str): The filename to save the serialized object to
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Load and return an instance of CustomObject from a file.

        Args:
            filename (str): The filename to load the object from

        Returns:
            CustomObject: An instance of CustomObject, or None if error occurs
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
