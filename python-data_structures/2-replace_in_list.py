#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """Replaces an element of a list at a specific position.

    Args:
        my_list: The list to modify.
        idx: The index of the element to replace.
        element: The new element to replace with.

    Returns:
        The modified list, or the original list if the index is out of range.
    """

    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list
