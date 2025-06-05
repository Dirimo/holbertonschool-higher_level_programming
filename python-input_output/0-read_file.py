#!/usr/bin/python3
"""
This module provides a function to read the contents of a file and print it.

Functions:
    read_file(filename=""): Reads the content of the specified
    file and prints it.
"""


def read_file(filename=""):
    """
    Reads a text file UTF8 and prints it to stdout


    Args:
        filename (str): The name of the file to read. Defaults
        to an empty string.
    """
    with open(filename, "r", enconding="utf-8") as file:
        read_data = file.read()
        print(read_data, end="")
