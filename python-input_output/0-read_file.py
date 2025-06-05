#!/usr/bin/python3
"""Defines text file and reading function"""


def read_file(filename=""):
    """Reads a text file UTF8 and prints it to stdout


    Args:
        filename (str): The nae of the file to read.
    """
    with open(filename, "r", enconding="utf-8") as file:
        read_data = file.read()    
        print(read_data, end="")
    
