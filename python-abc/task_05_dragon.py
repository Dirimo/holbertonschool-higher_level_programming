#!/usr/bin/python3
class SwimMixin:
    """
    A class mixin swimming functionality
    """
    def swim(self):
        """
        Prints the creature swims
        """
        print("The creature swim!")


class FlyMixin:
    """
    A class mixin flying functionality
    """

    def fly(self):
        """
        Prints the creature flies
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A class representing a dragon, inheriting from both SwimMixin and FlyMixin
    """

    def roar(self):
        """
        Prints he dragon roars
        """
        print("The dragon roars!")


if __name__ == "__main__":
    draco = Dragon()

    draco.swim()
    draco.fly()
    draco.roar()
