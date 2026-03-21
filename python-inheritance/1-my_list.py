#!/usr/bin/python3
"""
this module find sorted list
"""


class Mylist(list):
    """
    MyList class that inherits from the built-in list class.
    """

    def print_sorted(self):
        """
        this function prints list with sorted version
        """
        print(sorted(self))
