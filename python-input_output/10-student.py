#!/usr/bin/python3


class Student:
    """
    Defines a student by first_name, last_name and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        If attrs is a list of strings, only attribute names contained in
        this list must be retrieved.  Otherwise, all attributes must be
        retrieved.

        Args:
            attrs (list, optional): A list of attribute names to retrieve.
                Defaults to None.

        Returns:
            dict: A dictionary containing the specified attributes of the
                Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            json_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    json_dict[attr] = getattr(self, attr)
            return json_dict
