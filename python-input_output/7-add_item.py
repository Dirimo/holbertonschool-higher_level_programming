#!/usr/bin/python3
import sys
from os import path
from json import JSONDecodeError

# Assuming 5-save_to_json_file.py and 6-load_from_json_file.py
# are in the same directory and contain the functions
# save_to_json_file and load_from_json_file respectively.
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


def add_item_to_json_file(args, filename="add_item.json"):
    """Adds all arguments to a Python list and saves them to a JSON file.

    Args:
        args (list): List of arguments to add to the list.
        filename (str): The name of the JSON file to save to.
    """
    if path.exists(filename):
        try:
            my_list = load_from_json_file(filename)
        except JSONDecodeError:
            my_list = []
    else:
        my_list = []

    my_list.extend(args)
    save_to_json_file(my_list, filename)


if __name__ == "__main__":
    arguments = sys.argv[1:]  # Exclude the script name itself
    add_item_to_json_file(arguments)
