#!/usr/bin/python3
"""
Module to find the maximum integer in a list
"""


def max_integer(list=[]):
    """
    Finds the maximum integer in a list.
    If the list is empty, returns None.
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return resulti
