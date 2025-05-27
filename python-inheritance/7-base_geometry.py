#!/usr/bin/python3

class BaseGeometry:
    """
    A base class for geometry objects.
    """

    def area(self):
        """
        Calculates the area of the geometry object.

        Raises:
            Exception: If the area() method is not implemented.
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value.

        Args:
            name (str): The name of the value.
            value(int): The value to validate

        Raises:
            TypeError: If value is not an integer

            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater then 0")
