#!/usr/bin/python3
"""
This module defines a Student class with serialization and deserialization
methods.
"""


class Student:
    """
    A class that defines a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        pass

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): A list of strings with attribute names to retrieve.
                         If None, all attributes are retrieved.

        Returns:
            dict: Dictionary representation of the Student instance.
        """
        pass

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.

        Args:
            json (dict): A dictionary with attribute names as keys
                        and attribute values as values.
        """
        pass
