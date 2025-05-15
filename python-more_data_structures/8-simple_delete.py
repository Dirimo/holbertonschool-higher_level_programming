#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """Deletes a key in a dictionary.

    Args:
        a_dictionary: The dictionary to modify.
        key: The key to delete (string).
    """
    if key in a_dictionary:
        del a_dictionary[key]
