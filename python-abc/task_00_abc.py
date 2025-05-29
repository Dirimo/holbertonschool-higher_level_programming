#!/usr/bin/python3
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    An abstract base class for animals.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method to define the sound of the animal.
        """
        pass


class Dog(Animal):
    """
    A concrete class representing a dog.
    """

    def sound(self):
        """
        Returns the sound of a dog.
        """
        return "Bark"


class Cat(Animal):
    """
    A concrete class representing a cat.
    """

    def sound(self):
        """
        Returns the sound of a cat.
        """
        return "Meow"


if __name__ == "__main__":
    dog = Dog()
    cat = Cat()

    print(f"Dog says: {dog.sound()}")
    print(f"Cat says: {cat.sound()}")
