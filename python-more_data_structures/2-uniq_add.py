#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Adds all unique integers in a list (only once for each integer).

    Args:
        my_list: The list of integers.

    Returns:
        The sum of all unique integers in the list.
    """
    unique_integers = []
    for num in my_list:
        if num not in unique_integers:
            unique_integers.append(num)

    total = 0
    for num in unique_integers:
        total += num

    return total
