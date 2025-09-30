#!/usr/bin/env python3
"""
Basic serialization module.

This module provides functionality to serialize a
Python dictionary to a JSON file
and deserialize the JSON file to recreate
the Python Dictionary.
"""
import pickle


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.

    Args:
        data: A Python Dictionary with data
        filename: The filename of the output JSON file.
        If the output file
        already exists it should be replaced.
    """
    with open(filename, 'wb') as f:
        pickle.dump(data, f)


def load_and_deserialize(filename):
    """
    Load and deserialize data from a JSON file.

    Args:
        filename: The filename of the input JSON file

    Returns:
        A Python Dictionary with the deserialized JSON data from the file.
    """
    with open(filename, 'rb') as f:
        return pickle.load(f)
