#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """Replaces or adds key/value in a dictionary.

    Args:
        a_dictionary: The dictionary to update.
        key: The key to add or update (string).
        value: The value to associate with the key (any type).
    """
    a_dictionary[key] = value
