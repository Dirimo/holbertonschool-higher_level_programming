#!/usr/bin/python3
"""Defines a base geometry class BassGeometry"""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a parameter as an integer.

        Args:
            name (str): The name of the parameter
            value(int): The parameter to validate.

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is <= 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater then 0".format(name))
