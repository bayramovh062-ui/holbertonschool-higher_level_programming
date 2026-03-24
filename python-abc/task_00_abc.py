#!/usr/bin/python3
"""
this module explains abstract
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """
    this class represents animals
    """

    @abstractmethod
    def sound(self):
        """
        this is an abstractmethod that we should write
        sound function in each subclasses for this
        """

        pass


class Dog(Animal):
    """
    that is a class that represetns dog
    and this class inheritance from Animal
    """

    def sound(self):
        """
        this is a sound function that returns
        Bark message
        """

        return "Bark"


class Cat(Animal):
    """
    that is a class that represents dog
    and this class inheritance from animal
    """

    def sound(self):
        """
        this is a sound function that returns
        Meow message
        """

        return "Meow"
