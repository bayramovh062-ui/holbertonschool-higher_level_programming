#!/usr/bin/env python3
"""
this module explains multi inheritance with examples
"""


class Fish:
    """
    this class gives us information about fish
    """
    def swim(self):
        """
        this function prints information about fish's activity
        """
        print("The fish is swimming")

    def habitat(self):
        """
        this function prints information about fish's envoriment
        """
        print("The fish lives in water")


class Bird:
    """
    this class gives us information about bird
    """
    def fly(self):
        """
        this function prints information about bird's activity
        """
        print("The bird is flying")

    def habitat(self):
        """
        this function prints information about bird's envoriment
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    this class gives us information about fish and bird
    with use multi inheritance
    """

    def fly(self):
        """
        this function override fly method
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        this function override swim method
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        this function override habitat method
        """
        print("The flying fish lives both in water and the sky!")
