#!/usr/bin/python3
import json

"""Defines function that returns the JSON
representation of an object (string)"""


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)

    Args:
        my_obj: The Object to be serialized to JSON.


    Returns:
        str: The JSON string representation of the object.
    """

    return json.dumps(my_obj)
