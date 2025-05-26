#!/usr/bin/python3
"""
My list
"""


class Mylist(list):
    """
    Write a class Mylist that inherits from list
    """
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
