#!/usr/bin/python3
"""Defines text file and reading function"""


def read_file(filename=""):
    """Prints the content of a UTF8 texte file to stdout"""
    with open(filename, enconding="utf-8") as f:
        print(f.read(), end="")
