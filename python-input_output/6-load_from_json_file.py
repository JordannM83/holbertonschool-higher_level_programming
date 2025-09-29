#!/usr/bin/python3
"""
This module contains a function that creates an Object from a "JSON file".
"""
import json


def load_from_json_file(filename):
    """
    Creates an Object from a "JSON file".

    Args:
        filename (str): The name of the JSON file to load from.

    Returns:
        object: The object created from the JSON file.
    """
    with open(filename, encoding="UTF-8") as f:
        return json.loads(f.read())
