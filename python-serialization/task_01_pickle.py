#!/usr/bin/python3
"""
    serialize and deserialize custom python objects using the pickle module
"""

import pickle


class CustomObject:
    """
    A custom class with attributes name, age, and is_student,
    and methods to serialize and deserialize instances using pickle.
    """

    def __init__(self, name, age, is_student):
        """
        Initializes a CustomObject instance.

        Args:
            name (str): The name of the object.
            age (int): The age of the object.
            is_student (bool): Whether the object is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Prints the object's attributes in a formatted string.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the current instance to a file using pickle.

        Args:
            filename (str): The name of the file to serialize the object to.
        """
        try:
            with open(filename, 'wb') as myfile:
                pickle.dump(self, myfile)
            return True
        except (FileNotFoundError, IOError, pickle.PicklingError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes an instance of CustomObject from a file using pickle.

        Args:
            filename (str): The name of the file
            to deserialize the object from.

        Returns:
            CustomObject: An instance of CustomObject,
            or None if an error occurs.
        """
        try:
            with open(filename, 'rb') as myfile:
                loaded_data = pickle.load(myfile)
                if isinstance(loaded_data, cls):
                    return loaded_data
                return None
        except (FileNotFoundError, IOError, pickle.UnpicklingError, EOFError):
            return None
