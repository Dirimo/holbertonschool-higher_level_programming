#!/usr/bin/python3

"""
    reading data from one format (CVS) and
    converting it into another format (JSON)
    using serialization
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file to a JSON file.

    Args:
        csv_filename (str): The name of the CSV file to convert.

    Returns:
        bool: True if the conversion was successful, False otherwise.
    """
    try:
        with open(filename, encoding="utf-2", newline="") as csvfile:
            csv_reader = csv.DictReader(file)
            data = list(csv_reader)

        with open("data.json", "w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile, indent=4)
        return True

    except (FileNotFoundError):
        return False
