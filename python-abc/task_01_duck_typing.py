#!/usr/bin/python3
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    An abstract base class for shapes.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method to calculate the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to calculate the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    A concrete class representing a circle.
    """

    def __init__(self, radius):
        """
        Initializes a Circle object with a given radius.
        """
        self.radius = radius

    def area(self):
        """
        Calculates the area of the circle.
        """
        return math.pi * self.radius**2

    def perimeter(self):
        """
        Calculates the perimeter (circumference) of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    A concrete class representing a rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle object with a given width and height.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculates the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of a given shape.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 6)

    print("Circle:")
    shape_info(circle)

    print("\nRectangle:")
    shape_info(rectangle)
