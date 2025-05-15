#!/usr/bin/python3
def best_score(a_dictionary):
    """Returns a key with the biggest integer value.

    Args:
        a_dictionary: The dictionary to process.

    Returns:
        The key with the biggest integer value, or None if no score found.
    """
    if not a_dictionary:
        return None

    best_key = None
    best_score = float('-inf')  # Initialize with negative infinity

    for key, value in a_dictionary.items():
        if value > best_score:
            best_score = value
            best_key = key

    return best_key
