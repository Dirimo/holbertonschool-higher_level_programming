#!/usr/bin/python3
"""Defines a file-writing function"""


def write_file(filename="", text=""):
    """Writing a string to a text file (utf-8) and returns
    the number of characters written

    Args:
        filename (str): The name of the file to write to.
        text (str): The string to write to the file.

    Returns:
        int: The number of characters written.

    """

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
