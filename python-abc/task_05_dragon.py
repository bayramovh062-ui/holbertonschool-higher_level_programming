#!/usr/bin/env python3
"""
this module teaches how to create an object with used
two different class's properties
"""



class SwimMixin():
    """
    this class contains swim information
    """
    def swim(self):
        """
        this function prints swim information
        """
        print("The creature swims!")


class FlyMixin:
    """
    this class contains fly information
    """
    def fly(self):
        """
        this function prints fly information
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    that is an object that created by using swimmixin and flymixin
    """
    def roar(self):
        """
        this function prints dragon's roar
        """
        print("The dragon roars!")
