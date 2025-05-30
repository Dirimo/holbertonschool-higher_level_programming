#!/usr/bin/python3
class Fish:
    """
    A class representing a fish.
    """

    def swim(self):
        """
        Prints that the fish is swimming.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Prints the habitat of the fish.
        """
        print("The fish lives in water")


class Bird:
    """
    A class representing a bird.
    """

    def fly(self):
        """
        Prints that the bird is flying.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Prints the habitat of the bird.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    A class representing a flying fish, inheriting from both Fish and Bird.
    """

    def fly(self):
        """
        Overrides the fly method to describe the flying fish soaring.
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Overrides the swim method to describe the flying fish swimming.
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Overrides the habitat method to describe the flying fish's habitat.
        """
        print("The flying fish lives both in water and the sky!")


if __name__ == "__main__":
    flying_fish = FlyingFish()

    flying_fish.swim()
    flying_fish.fly()
    flying_fish.habitat()

    print("\nMethod Resolution Order (MRO):")
    print(FlyingFish.mro())
