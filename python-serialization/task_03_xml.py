#!/usr/bin/env python3
"""
XML serialization and deserialization module.

This module explores serialization and deserialization using XML as an
alternative format to JSON.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into XML and save it to a file.

    Args:
        dictionary (dict): The Python dictionary to serialize
        filename (str): The filename to save the XML data to
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Read XML data from a file and return a deserialized Python dictionary.

    Args:
        filename (str): The filename to read XML data from

    Returns:
        dict: The deserialized Python dictionary
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}
        for child in root:
            result[child.tag] = child.text

        return result
    except (ET.ParseError, FileNotFoundError):
        return None
