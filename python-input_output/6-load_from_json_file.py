#!/usr/bin/python3
import json
"""Defines a function to create an object"""


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”.

    Args:
        filename (str): The name of the JSON file to load from.

    Returns:
        object: The Python object represented by the JSON data in the file.
    """

    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
