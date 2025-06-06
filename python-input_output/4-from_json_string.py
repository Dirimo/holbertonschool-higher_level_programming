#!/usr/bin/python3

"""
This module provides a function that returns an object
(Python data structure) represented by a JSON string.

Functions:
    from_json_string(my_str): Returns an object represented
    by a JSON string.
"""

import json


def from_json_string(my_str):
    """Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): The JSON string to be converted to a Python object.

    Returns:
        object: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
