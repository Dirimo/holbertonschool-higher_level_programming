#!/usr/bin/python3i
"""
    Module to serialize / deserialize
"""

import json


def serialize_and_save_to_file(data, filename):
    """Serializes a Python dictionary to JSON and saves it to a file.

    Args:
        data (dict): The Python dictionary to serialize.
        filename (str): The name of the file to save the JSON data to.
    """
    with open(filename, "w") as myfile:
        json.dump(data, myfile, indent=4)


def load_and_deserialize(filename):
    """Loads JSON data from a file and deserializes it
    into a Python dictionary.
    Args:
        filename (str): The name of the file to load the JSON data from.
    Returns:
        dict: The Python dictionary deserialized
        from the JSON data, or None if an error occurs.
    """
    with open(filename, "r") as myfile:
        data = json.load(myfile)
    return data
