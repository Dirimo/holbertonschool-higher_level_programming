#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Replaces an element in a list at a specific position
    without modifying the original list.

    Args:
        my_list: The list to modify.
        idx: The index of the element to replace.
        element: The new element.

    Returns:
        A new list with the element replaced, or a copy of the
        original list if idx is out of range.
    """
    new_list = my_list.copy()
    if (idx >= 0 and len(new_list) > idx):
        new_list[idx] = element
    return new_list
