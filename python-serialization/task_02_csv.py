#!/usr/bin/env python3
"""
CSV to JSON conversion module.

This module provides functionality to read data from CSV format and convert it
into JSON format using serialization techniques.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert CSV data to JSON format.

    Args:
        csv_filename (str): The CSV filename to read data from

    Returns:
        bool: True if the conversion was successful, False otherwise
    """
    with open(csv_filename, mode='r', newline='', encoding='utf-8') as csvfile:
        data = list(csv.DictReader(csvfile))

    with open('data.json', mode='w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4)
