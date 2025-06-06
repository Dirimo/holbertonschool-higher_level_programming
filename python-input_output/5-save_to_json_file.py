#!/usr/bin/python3
"""Module containing save_to_json_file function"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation.

    Args:
        my_obj: The object to be serialized to JSON and written to the file.
        filename (str): The name of the file to write to.
    """

    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
