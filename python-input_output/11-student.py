#!/usr/bin/python3
"""
This module defines a Student class with filtering capability.
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
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): A list of strings with attribute names to retrieve.
                         If None, all attributes are retrieved.

        Returns:
            dict: Dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            dict_attrs = {}
            for attr in attrs:
                if attr in self.__dict__:
                    dict_attrs[attr] = self.__dict__[attr]
        return dict_attrs


    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.

        Args:
            json (dict): A dictionary with attribute names as keys
                        and attribute values as values.
        """
        for key, value in json.items():
            setattr(self, key, value)
